import os.path

from .lib_local.svt_local import *
from .lib_local.cft_local import *
from .lib_local.cmd_local import *
from hoshino.typing import CQEvent


@sv_lib.on_fullmatch(("帮助fgo图书馆", "帮助FGO图书馆", "帮助bgo图书馆", "帮助BGO图书馆"))
@sv_lib.on_rex(re.compile(r"^[fb]go[图tl][书si][馆gb][帮b][助z]$", re.IGNORECASE))
async def bangzhu(bot: HoshinoBot, ev: CQEvent):
    helps = gen_node(sv_lib_help)
    await bot.send_group_forward_msg(group_id=ev['group_id'], messages=helps)


@sv_lib.on_rex(re.compile(r"^[获h更g][取q新x][fb]go[图tl][书si][馆gb](\s.+)?$", re.IGNORECASE))
async def update_lib(bot: HoshinoBot, ev: CQEvent):
    try:
        with open(all_servant_path, 'r', encoding="utf-8") as f:
            svt = json.load(f)
        with open(all_craft_path, 'r', encoding="utf-8") as f:
            cft = json.load(f)
        with open(all_command_path, 'r', encoding="utf-8") as f:
            cmd = json.load(f)
        with open(update_data_path, 'r', encoding="utf-8") as f:
            updates = json.load(f)
    except json.decoder.JSONDecodeError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆] 或 [获取全部内容]")
    except FileNotFoundError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆] 或 [获取全部内容]")

    crt_file = False
    group_config = load_config(ev, True)
    if not group_config["crt_path"] == "False":
        crt_file = os.path.join(crt_folder_path, group_config["crt_path"])

    update_svt = False
    update_cft = False
    update_cmd = False
    latest = False

    rule = re.compile(
        r"^[获h更g][取q新x][fb]go[图tl][书si][馆gb]\s?([最z][新x]|latest|recent)?$",
        re.IGNORECASE
    )
    rule_svt = re.compile(r"([从c][者z]|svt|servant)", re.IGNORECASE)
    rule_cft = re.compile(r"([礼l][装z]|cft|craft)", re.IGNORECASE)
    rule_cmd = re.compile(r"([纹w][章z]|cmd|command)", re.IGNORECASE)
    rule_latest = re.compile(r"([最z][新x]|latest|recent)", re.IGNORECASE)

    msg = ev.message.extract_plain_text()

    if re.match(rule, msg):
        update_svt = True
        update_cft = True
        update_cmd = True

    if re.search(rule_svt, msg):
        update_svt = True

    if re.search(rule_cft, msg):
        update_cft = True

    if re.search(rule_cmd, msg):
        update_cmd = True

    if re.search(rule_latest, msg):
        latest = True

    await bot.send(ev, "开始更新大图书馆~")

    if update_svt:
        sv_lib.logger.info("开始更新从者……")
        errors = []

        if latest:
            try:
                with open(lib_servant_path, 'r', encoding="utf-8") as f:
                    servants = json.load(f)
            except json.decoder.JSONDecodeError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆 + 从者]")
            except FileNotFoundError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆 + 从者]")

            svt_latest_local = int(servants[0]["id"])
            svt_latest_remote = int(svt[0]["id"])
            svt_ids = [int(servants[i_svt]["id"]) for i_svt in range(len(servants))]
            svt_ids.sort(reverse=True)
            svt_ids = list(map(str, svt_ids))
            if not svt_latest_local == svt_latest_remote or updates["svt"]:
                update_svt_list = list(map(int, updates["svt"]))
                update_svt_list.sort()
                update_svt_list = list(map(str, update_svt_list))
                for each_update_svt_id in update_svt_list:
                    try:
                        ready_svt = [each_svt for each_svt in svt if each_svt.get("id") == each_update_svt_id][0]
                    except IndexError:
                        sv.logger.info(f"no id: {each_update_svt_id}")
                        await bot.send(ev, f"不存在的从者id：{each_update_svt_id}")
                        continue
                    svt_data = await lib_svt(ready_svt, crt_file)
                    if each_update_svt_id in svt_ids:
                        servants[svt_ids.index(each_update_svt_id)] = svt_data
                    else:
                        servants.insert(0, svt_data)
                    if "error" in svt_data:
                        sv_lib.logger.error(f"更新从者{each_update_svt_id}出错：{svt_data['error']}")
                        errors.append(each_update_svt_id)

            updates["svt"] = []

        else:
            servants = []
            # data = await lib_svt(svt[23], crt_file)
            for each_svt in svt:
                data = await lib_svt(each_svt, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新从者{each_svt['id']}出错：{data['error']}")
                    errors.append(each_svt["id"])
                servants.append(data)

        if os.path.exists(lib_servant_path):
            try:
                old_servants = json.load(open(lib_servant_path, encoding="utf-8"))
                if old_servants == servants:
                    await bot.send(ev, "从者无需更新~")
                else:
                    with open(lib_servant_path, "w", encoding="utf-8") as f:
                        f.write(json.dumps(servants, indent=2, ensure_ascii=False))
                    await bot.send(ev, "已获取从者数据~")
                    if errors:
                        e_msg = "以下从者出错，请单独获取："
                        for error in errors:
                            e_msg += f"{error}; "
                        await bot.send(ev, e_msg)
            except json.decoder.JSONDecodeError:
                pass
        else:
            with open(lib_servant_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(servants, indent=2, ensure_ascii=False))
            await bot.send(ev, "已获取从者数据~")
            if errors:
                e_msg = "以下从者出错，请单独获取："
                for error in errors:
                    e_msg += f"\t{error}"
                await bot.send(ev, e_msg)

    if update_cft:
        sv_lib.logger.info("开始更新礼装……")
        errors = []

        if latest:
            try:
                with open(lib_craft_path, 'r', encoding="utf-8") as f:
                    crafts = json.load(f)
            except json.decoder.JSONDecodeError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")
            except FileNotFoundError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")

            cft_latest_local = int(crafts[0]["id"])
            cft_latest_remote = int(cft[0]["id"])
            cft_ids = [int(crafts[i_cft]["id"]) for i_cft in range(len(crafts))]
            cft_ids.sort(reverse=True)
            cft_ids = list(map(str, cft_ids))
            if not cft_latest_local == cft_latest_remote or updates["cft"]:
                update_cft_list = list(map(int, updates["cft"]))
                update_cft_list.sort()
                update_cft_list = list(map(str, update_cft_list))
                for each_update_cft_id in update_cft_list:
                    try:
                        ready_cft = [each_cft for each_cft in cft if each_cft.get("id") == each_update_cft_id][0]
                    except IndexError:
                        sv.logger.info(f"no id: {each_update_cft_id}")
                        await bot.send(ev, f"不存在的礼装id：{each_update_cft_id}")
                        continue
                    cft_data = await lib_cft(ready_cft, crt_file)
                    if each_update_cft_id in cft_ids:
                        crafts[cft_ids.index(each_update_cft_id)] = cft_data
                    else:
                        crafts.insert(0, cft_data)
                    if "error" in cft_data:
                        sv_lib.logger.error(f"更新礼装{each_update_cft_id}出错：{cft_data['error']}")
                        errors.append(each_update_cft_id)

            updates["cft"] = []

        else:
            crafts = []

            # data = await lib_cft(cft[0], crt_file)
            for each_cft in cft:
                data = await lib_cft(each_cft, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新礼装{each_cft['id']}出错：{data['error']}")
                    errors.append(each_cft["id"])
                crafts.append(data)

        if os.path.exists(lib_craft_path):
            try:
                old_crafts = json.load(open(lib_craft_path, encoding="utf-8"))
                if old_crafts == crafts:
                    await bot.send(ev, "礼装无需更新~")
                else:
                    with open(lib_craft_path, "w", encoding="utf-8") as f:
                        f.write(json.dumps(crafts, indent=2, ensure_ascii=False))
                    await bot.send(ev, "已获取礼装数据~")
                    if errors:
                        e_msg = "以下礼装出错，请单独获取："
                        for error in errors:
                            e_msg += f"{error}\t"
                        await bot.send(ev, e_msg)
            except json.decoder.JSONDecodeError:
                pass
        else:
            with open(lib_craft_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(crafts, indent=2, ensure_ascii=False))
            await bot.send(ev, "已获取礼装数据~")
            if errors:
                e_msg = "以下礼装出错，请单独获取："
                for error in errors:
                    e_msg += f"{error}\t"
                await bot.send(ev, e_msg)

    if update_cmd:
        sv_lib.logger.info("开始更新纹章……")
        errors = []

        if latest:
            try:
                with open(lib_command_path, 'r', encoding="utf-8") as f:
                    commands = json.load(f)
            except json.decoder.JSONDecodeError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")
            except FileNotFoundError:
                await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")

            cmd_latest_local = int(commands[0]["id"])
            cmd_latest_remote = int(cmd[0]["id"])
            cmd_ids = [int(commands[i_cmd]["id"]) for i_cmd in range(len(commands))]
            cmd_ids.sort(reverse=True)
            cmd_ids = list(map(str, cmd_ids))
            if not cmd_latest_local == cmd_latest_remote or updates["cmd"]:
                update_cmd_list = list(map(int, updates["cmd"]))
                update_cmd_list.sort()
                update_cmd_list = list(map(str, update_cmd_list))
                for each_update_cmd_id in update_cmd_list:
                    try:
                        ready_cmd = [each_cmd for each_cmd in cmd if each_cmd.get("id") == each_update_cmd_id][0]
                    except IndexError:
                        sv.logger.info(f"no id: {each_update_cmd_id}")
                        await bot.send(ev, f"不存在的纹章id：{each_update_cmd_id}")
                        continue
                    cmd_data = await lib_cmd(ready_cmd, crt_file)
                    if each_update_cmd_id in cmd_ids:
                        commands[cmd_ids.index(each_update_cmd_id)] = cmd_data
                    else:
                        commands.insert(0, cmd_data)
                    if "error" in cmd_data:
                        sv_lib.logger.error(f"更新纹章{each_update_cmd_id}出错：{cmd_data['error']}")
                        errors.append(each_update_cmd_id)

            updates["cmd"] = []

        else:
            commands = []

            # data = await lib_cmd(cft[0], crt_file)
            for each_cmd in cmd:
                data = await lib_cmd(each_cmd, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新纹章{each_cmd['id']}出错：{data['error']}")
                    errors.append(each_cmd["id"])
                commands.append(data)

        if os.path.exists(lib_command_path):
            try:
                old_commands = json.load(open(lib_command_path, encoding="utf-8"))
                if old_commands == commands:
                    await bot.send(ev, "纹章无需更新~")
                else:
                    with open(lib_command_path, "w", encoding="utf-8") as f:
                        f.write(json.dumps(commands, indent=2, ensure_ascii=False))
                    await bot.send(ev, "已获取纹章数据~")
                    if errors:
                        e_msg = "以下纹章出错，请单独获取："
                        for error in errors:
                            e_msg += f"{error}\t"
                        await bot.send(ev, e_msg)
            except json.decoder.JSONDecodeError:
                pass
        else:
            with open(lib_command_path, "w", encoding="utf-8") as f:
                f.write(json.dumps(commands, indent=2, ensure_ascii=False))
            await bot.send(ev, "已获取纹章数据~")
            if errors:
                e_msg = "以下纹章出错，请单独获取："
                for error in errors:
                    e_msg += f"{error}\t"
                await bot.send(ev, e_msg)

    with open(update_data_path, "w", encoding="utf-8") as f:
        f.write(json.dumps(updates, indent=2, ensure_ascii=False))


@sv_lib.on_rex(re.compile(r"^[查c][询x][fb]go[图tl][书si][馆gb](\s[\s\S]+)?$", re.IGNORECASE))
async def check_lib(bot: HoshinoBot, ev: CQEvent):
    try:
        with open(all_servant_path, 'r', encoding="utf-8") as f:
            svt = json.load(f)
        with open(all_craft_path, 'r', encoding="utf-8") as f:
            cft = json.load(f)
        with open(all_command_path, 'r', encoding="utf-8") as f:
            cmd = json.load(f)
        with open(lib_servant_path, 'r', encoding="utf-8") as f:
            servants = json.load(f)
        with open(lib_craft_path, 'r', encoding="utf-8") as f:
            crafts = json.load(f)
        with open(lib_command_path, 'r', encoding="utf-8") as f:
            commands = json.load(f)
    except json.decoder.JSONDecodeError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[获取全部内容]")
    except FileNotFoundError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[获取全部内容]")

    rule_svt = re.compile(r"([从c][者z]|svt|servant)", re.IGNORECASE)
    rule_cft = re.compile(r"([礼l][装z]|cft|craft)", re.IGNORECASE)
    rule_cmd = re.compile(r"([纹w][章z]|cmd|command)", re.IGNORECASE)
    args = ev.message.extract_plain_text()
    msg = ""

    if re.search(rule_svt, args):
        msg += f"从者：\n远程：{svt[0]['name_cn']}\tid：{svt[0]['id']}\n"
        msg += f"从者：\n本地：{servants[0]['name_cn']}\tid：{servants[0]['id']}\n"

    if re.search(rule_cft, args):
        msg += f"礼装：\n远程：{cft[0]['name']}\tid：{cft[0]['id']}\n"
        msg += f"礼装：\n本地：{crafts[0]['name']}\tid：{crafts[0]['id']}\n"

    if re.search(rule_cmd, args):
        msg += f"纹章：\n远程：{cmd[0]['name']}\tid：{cmd[0]['id']}\n\n"
        msg += f"纹章：\n本地：{commands[0]['name']}\tid：{commands[0]['id']}\n\n"

    await bot.finish(ev, msg.strip())


@sv_lib.on_rex(re.compile(r"^(增添|add)[fb]go[图tl][书si][馆gb](\s.+)?(\s\d+)?$", re.IGNORECASE))
async def add_lib(bot: HoshinoBot, ev: CQEvent):
    try:
        with open(all_servant_path, 'r', encoding="utf-8") as f:
            svt = json.load(f)
        with open(all_craft_path, 'r', encoding="utf-8") as f:
            cft = json.load(f)
        with open(all_command_path, 'r', encoding="utf-8") as f:
            cmd = json.load(f)
    except json.decoder.JSONDecodeError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[获取全部内容]")
    except FileNotFoundError:
        await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[获取全部内容]")

    crt_file = False
    if os.path.exists(config_path):
        try:
            configs = json.load(open(config_path, encoding="utf-8"))
            for each_group in configs["groups"]:
                if each_group["group"] == ev.group_id:
                    if not each_group["crt_path"] == "False":
                        crt_file = os.path.join(crt_folder_path, each_group["crt_path"])
                        break
        except json.decoder.JSONDecodeError:
            pass

    update_svt = False
    update_cft = False
    update_cmd = False

    rule_svt = re.compile(r"([从c][者z]|svt|servant)", re.IGNORECASE)
    rule_cft = re.compile(r"([礼l][装z]|cft|craft)", re.IGNORECASE)
    rule_cmd = re.compile(r"([纹w][章z]|cmd|command)", re.IGNORECASE)

    msg = ev.message.extract_plain_text().split()
    if not len(msg) == 3:
        await bot.finish(ev, "食用指南：增添fgo图书馆 + 类型 + id")

    if re.search(rule_svt, msg[1]):
        update_svt = True

    if re.search(rule_cft, msg[1]):
        update_cft = True

    if re.search(rule_cmd, msg[1]):
        update_cmd = True

    if update_svt:
        sv_lib.logger.info("开始增添从者……")

        try:
            with open(lib_servant_path, 'r', encoding="utf-8") as f:
                servants = json.load(f)
        except json.decoder.JSONDecodeError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")
        except FileNotFoundError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")

        # data = await lib_svt(svt[23], crt_file)
        data = None
        if not int(msg[2]) > int(servants[0]["id"]):
            await bot.finish(ev, "此从者本地已有数据~更新从者数据请使用[修补fgo图书馆 + 从者 + id]")

        if not int(msg[2]) == int(servants[0]["id"]) + 1:
            await bot.finish(ev, f"此id前还存在未增添的从者~本地最新id：{servants[0]['id']}")

        for each_svt in svt:
            if msg[2] == each_svt["id"]:
                data = await lib_svt(each_svt, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新从者{each_svt['id']}出错：{data['error']}")
                    await bot.send(ev, f"更新从者{each_svt['id']}出错：{data['error']}")
                break

        if data is None:
            await bot.finish(ev, "不存在此id~")

        servants.insert(0, data)

        with open(lib_servant_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(servants, indent=2, ensure_ascii=False))
        await bot.finish(ev, "已获取从者数据~")

    if update_cft:
        sv_lib.logger.info("开始更新礼装……")

        try:
            with open(lib_craft_path, 'r', encoding="utf-8") as f:
                crafts = json.load(f)
        except json.decoder.JSONDecodeError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")
        except FileNotFoundError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")

        # data = await lib_cft(cft[0], crt_file)
        data = None
        if not int(msg[2]) > int(crafts[0]["id"]):
            await bot.finish(ev, "此礼装本地已有数据~更新礼装数据请使用[修补fgo图书馆 + 礼装 + id]")

        if not int(msg[2]) == int(crafts[0]["id"]) + 1:
            await bot.finish(ev, f"此id前还存在未增添的礼装~本地最新id：{crafts[0]['id']}")

        for each_cft in cft:
            if msg[2] == each_cft["id"]:
                data = await lib_cft(each_cft, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新礼装{each_cft['id']}出错：{data['error']}")
                    await bot.send(ev, f"更新礼装{each_cft['id']}出错：{data['error']}")
                break

        if data is None:
            await bot.finish(ev, "不存在此id~")

        crafts.insert(0, data)

        with open(lib_craft_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(crafts, indent=2, ensure_ascii=False))
        await bot.finish(ev, "已获取礼装数据~")

    if update_cmd:
        sv_lib.logger.info("开始更新纹章……")

        try:
            with open(lib_command_path, 'r', encoding="utf-8") as f:
                commands = json.load(f)
        except json.decoder.JSONDecodeError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")
        except FileNotFoundError:
            await bot.finish(ev, "本地没有数据~请先获取数据~\n指令：[更新fgo图书馆]")

        # data = await lib_cmd(cft[0], crt_file)
        data = None
        if not int(msg[2]) > int(commands[0]["id"]):
            await bot.finish(ev, "此纹章本地已有数据~更新纹章数据请使用[修补fgo图书馆 + 纹章 + id]")

        if not int(msg[2]) == int(commands[0]["id"]) + 1:
            await bot.finish(ev, f"此id前还存在未增添的纹章~本地最新id：{commands[0]['id']}")

        for each_cmd in cmd:
            if msg[2] == each_cmd["id"]:
                data = await lib_cmd(each_cmd, crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新纹章{each_cmd['id']}出错：{data['error']}")
                    await bot.send(ev, f"更新纹章{each_cmd['id']}出错：{data['error']}")
                break

        if data is None:
            await bot.finish(ev, "不存在此id~")

        crafts.insert(0, data)

        with open(lib_command_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(commands, indent=2, ensure_ascii=False))
        await bot.finish(ev, "已获取纹章数据~")


@sv_lib.on_rex(re.compile(
    r"^[修x][补b][fb]go"
    r"([图tl][书si][馆gb]|([从c][者z]|svt|servant)|([礼l][装z]|cft|craft)|([纹w][章z]|cmd|command))"
    r"(\s.+)?$", re.IGNORECASE
))
async def fix_lib(bot: HoshinoBot, ev: CQEvent):
    is_3_args = False
    rule_raw = re.compile(r"^([修x])?([补b])?[fb]go[图tl][书si][馆gb]([修x])?([补b])?(\s.+)?$", re.IGNORECASE)
    if re.match(rule_raw, ev.raw_message):
        is_3_args = True

    msg = ev.message.extract_plain_text().split()

    if is_3_args:
        if not len(msg) == 3:
            await bot.finish(ev, "食用指南：[修补fgo图书馆 + 类型 + id]")

        if not msg[2].isdigit():
            await bot.finish(ev, "说了要id，宁这是填了个🔨")
    else:
        if not len(msg) == 2:
            await bot.finish(ev, "食用指南：[修补fgo(类型) + id]")

        if not msg[1].isdigit():
            await bot.finish(ev, "说了要id，宁这是填了个🔨")

    try:
        with open(lib_servant_path, 'r', encoding="utf-8") as f:
            svt = json.load(f)
        with open(lib_craft_path, 'r', encoding="utf-8") as f:
            cft = json.load(f)
        with open(lib_command_path, 'r', encoding="utf-8") as f:
            cmd = json.load(f)
        with open(all_servant_path, 'r', encoding="utf-8") as f:
            servants = json.load(f)
        with open(all_craft_path, 'r', encoding="utf-8") as f:
            crafts = json.load(f)
        with open(all_command_path, 'r', encoding="utf-8") as f:
            commands = json.load(f)
    except json.decoder.JSONDecodeError or FileNotFoundError:
        await bot.finish(ev, "本地没有图书馆数据~请先更新图书馆~\n指令：[更新fgo图书馆]")
    except FileNotFoundError:
        await bot.finish(ev, "本地没有图书馆数据~请先更新图书馆~\n指令：[更新fgo图书馆]")

    crt_file = False
    if os.path.exists(config_path):
        try:
            configs = json.load(open(config_path, encoding="utf-8"))
            for each_group in configs["groups"]:
                if each_group["group"] == ev.group_id:
                    if not each_group["crt_path"] == "False":
                        crt_file = os.path.join(crt_folder_path, each_group["crt_path"])
                        break
        except json.decoder.JSONDecodeError:
            pass

    rule_svt = re.compile(r"([从c][者z]|svt|servant)", re.IGNORECASE)
    is_svt = False
    if re.search(rule_svt, msg[1]):
        is_svt = True
        msg = msg[2:]
    if re.search(rule_svt, msg[0]):
        is_svt = True
        msg = msg[1:]

    fixed = False
    if is_svt:
        max_id = svt[0]["id"]
        if int(msg[0]) > int(max_id):
            await bot.finish(ev, "不存在此id，如果要新增条目请使用[增添fgo图书馆]~")
        for each_svt in svt:
            if each_svt["id"] == msg[0]:
                svt_index = svt.index(each_svt)
                data = await lib_svt(servants[svt_index], crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新从者{each_svt['id']}出错：{data['error']}")
                else:
                    fixed = True
                svt[svt_index] = data
                break

        with open(lib_servant_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(svt, indent=2, ensure_ascii=False))
        if fixed:
            await bot.finish(ev, "已修补从者数据~")
        else:
            await bot.finish(ev, "从者数据错误，请再试一次~")

    rule_cft = re.compile(r"([礼l][装z]|cft|craft)", re.IGNORECASE)
    is_cft = False
    if re.search(rule_cft, msg[1]):
        is_cft = True
        msg = msg[2:]
    if re.search(rule_cft, msg[0]):
        is_cft = True
        msg = msg[1:]

    fixed = False
    if is_cft:
        max_id = cft[0]["id"]
        if int(msg[0]) > int(max_id):
            await bot.finish(ev, "不存在此id，如果要新增条目请使用[增添fgo图书馆]~")
        for each_cft in cft:
            if each_cft["id"] == msg[0]:
                cft_index = cft.index(each_cft)
                data = await lib_cft(crafts[cft_index], crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新礼装{each_cft['id']}出错：{data['error']}")
                else:
                    fixed = True
                cft[cft_index] = data
                break

        with open(lib_craft_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(cft, indent=2, ensure_ascii=False))
        if fixed:
            await bot.finish(ev, "已修补礼装数据~")
        else:
            await bot.finish(ev, "礼装数据错误，请再试一次~")

    rule_cmd = re.compile(r"([纹w][章z]|cmd|command)", re.IGNORECASE)
    is_cmd = False
    if re.search(rule_cmd, msg[1]):
        is_cmd = True
        msg = msg[2:]
    if re.search(rule_cmd, msg[0]):
        is_cmd = True
        msg = msg[1:]

    fixed = False
    if is_cmd:
        max_id = cmd[0]["id"]
        if int(msg[0]) > int(max_id):
            await bot.finish(ev, "不存在此id，如果要新增条目请使用[增添fgo图书馆]~")
        for each_cmd in cmd:
            if each_cmd["id"] == msg[0]:
                cmd_index = cmd.index(each_cmd)
                data = await lib_cmd(commands[cmd_index], crt_file)
                if "error" in data:
                    sv_lib.logger.error(f"更新纹章{each_cmd['id']}出错：{data['error']}")
                else:
                    fixed = True
                cmd[cmd_index] = data
                break

        with open(lib_craft_path, "w", encoding="utf-8") as f:
            f.write(json.dumps(cmd, indent=2, ensure_ascii=False))
        if fixed:
            await bot.finish(ev, "已修补纹章数据~")
        else:
            await bot.finish(ev, "纹章数据错误，请再试一次~")


@sv_lib.on_rex(re.compile(r"^[查c][询x][fb]go([从c][者z]|svt|servant)(\s.+)?$", re.IGNORECASE))
async def find_svt(bot: HoshinoBot, ev: CQEvent):
    await local_find_svt(bot, ev)


@sv_lib.on_rex(re.compile(r"^[查c][询x][fb]go([礼l][装z]|cft|craft)(\s.+)?$", re.IGNORECASE))
async def find_cft(bot: HoshinoBot, ev: CQEvent):
    await local_find_cft(bot, ev)


@sv_lib.on_rex(re.compile(r"^[查c][询x][fb]go([纹w][章z]|cmd|command)(\s.+)?$", re.IGNORECASE))
async def find_cmd(bot: HoshinoBot, ev: CQEvent):
    await local_find_cmd(bot, ev)
