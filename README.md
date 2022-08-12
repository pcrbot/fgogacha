<!--suppress HtmlDeprecatedAttribute -->
<div align="center">

# Fate Grand Order Gacha Simulator

</div>

<div align="center">
    <img src="https://img.shields.io/github/v/release/kcn3388/fgogacha" alt="">
    <img src="https://img.shields.io/github/release-date/kcn3388/fgogacha" alt="">
    <img src="https://img.shields.io/github/license/kcn3388/fgogacha" alt="">
</div>

<div align="center">
<br>

FGO 模拟抽卡插件 for [HoshinoBot](https://github.com/Ice-Cirno/HoshinoBot)<br>
GitHub与问题反馈: https://github.com/kcn3388/fgogacha <br>
WIKI：https://github.com/kcn3388/fgogacha/wiki <br>

</div>

<div align="center">

### 要是觉得好用可以点个小星星呀

</div>

更新日志
======

### 2022
#### ※建议更新后清除全部配置文件并重新生成，每次更新会尽可能兼容之前的配置文件，但是出现问题请先排查配置文件的问题
- 🚀 v1.5.1 (2022-08-12)
  - 拆分下载全部资源，以方便了解进度
  - 修复当从者是所罗门/兽的时候的资源错误
- 🚀 v1.5.0 (2022-08-12)
  - 新功能：获取全部从者/礼装/纹章
    - 指令：``获取全部从者/礼装/纹章``
    - 获取全部从者包括图标，全服名称，指令卡配置，宝具卡色，昵称，入手方式
    - 获取全部礼装包括图标，礼装技能图标
    - 获取全部纹章包括图标，纹章技能图标
    - 下载上述内容，指令：``下载全部卡片资源``
    - **※此功能下载的数据并非抽卡模拟器所必须的资源**
  - 修复了几个潜在的bug
  - 现在会正确提示资源已下载
- 🚀 v1.4.1 (2022-08-10)
  - 新功能：现在更改更新时间间隔后会自动重载机器人
- 🚀 v1.4.0 (2022-08-10)
  - 新功能：手动设置自动更新时间间隔
    - 指令：``设置fgo时间 + 小时 + 分钟 + 秒``
      - 例如：``设置fgo时间 1小时60分钟60秒``
      - 至少输入其中一个时间参数
      - 由于HoshinoBot的定时工作逻辑，设置完成后需要重启机器人
- 🚀 v1.3.3 (2022-08-10)
  - 修正了几个潜在的bug
    - 由于QQ对消息风控的关系，对新闻发送机制进行调整：
      - 当无法使用卡片发送时，尝试直接发送（可能导致刷屏）
      - 当无法直接发送时，推送标题以及官网链接
      - 查询全部新闻机制：当无法合并发送时，拆分为单个卡片发送
      - 单个卡片发送失败时，处理方式同上
- 🚀 v1.3.2 (2022-08-09)
  - 修正了几个潜在的bug
  - 现在定期工作可以自定义时间了，单位为分钟
    - 定期工作现在会调用配置文件中第一个群的crt文件，如果不存在配置文件或crt文件未配置则会调用插件下的crt文件
  - 修改了默认crt路径，现在crt默认路径在插件目录下crt文件夹，自定义crt文件也请移动到此文件夹
  - **※现在请务必保证存在crt目录以及默认crt文件！**
- 🚀 v1.3.1 (2022-08-05)
  - 修正了几个潜在的bug
    - 现在池子没有更新的情况下会提醒无需更新卡池
    - 修改了配置文件格式，现在是否跟随最新卡池全局生效，不再单独跟随群配置
    - 修正了若自动更新池子时最新池子为日替池会导致抽卡失败的问题
      - 现在最新卡池若是日替池，默认会选择0号池
- 🚀 v1.3.0 (2022-08-04)
  - 新功能：获取官网新闻
    - ``[获取fgo新闻 + 数量]`` 从官网获取公告新闻，默认6条，置顶的概率公告会去掉
    - ``[查询fgo新闻 + 编号/all]`` 从本地查询公告具体内容，all代表全部获取
    - 修了几个潜在问题
- 🚀 v1.2.1 (2022-08-03)
  - 优化了正则表达式
- 🚀 v1.2.0 (2022-08-02)
  - 修复了几个潜在问题
    - 现在卡池更新不会乱序了，以mooncell页面的顺序为准，同时现在只会使用页面内的卡池，侧边栏卡池不再读取
    - 解决了侧边栏卡池与页面卡池重复的问题，顺带解决了去重时导致的乱序
    - 修复了因为配置文件为空导致的报错
  - 现在卡池更新以后全部群的卡池会重置指定卡池，默认是最新国服卡池，可以通过命令更改为国服剧情卡池
  - 增加自动更新卡池功能，自动更新卡池会追随最新国服卡池
- 🚀 v1.1.1 (2022-08-01)
  - 优化代码
- 🚀 v1.1.0 (2022-07-28)
    - 新功能：自定义crt验证文件以规避mooncell的拒绝访问
        - 如何获取证书请自行Google
        - 食用指南：``fgo_enable_crt + 证书路径``
            - 文件默认根路径：hoshino的res文件夹
            - 当不存在配置文件时不调用crt验证
            - 未指定证书路径时默认调用``ca-certificates.crt``
            - 未找到证书时尝试不调用crt验证
            - 不需要crt验证时请将证书路径设置为``False``
                - ``False``使用正则表达式支持全字大小写
            - ``fgo_check_crt``指令可用于检查是否存在配置文件，以及crt文件路径和是否禁用
- 🚀 v1.0.4 (2022-07-27)
    - 修正日替池子不正确的bug
    - 将所有触发词改为正则表达式触发，现在可以使用拼音缩写进行命令触发
        - 如：``切换fgo卡池`` → ``qhfgokc``
        - ~~主要是方便调试~~
- 🚀 v1.0.3 (2022-07-27)
    - 修改触发方式为正则表达式，不再需要atbot，现在可以同时检测\[fgo/bgo/FGO/BGO\]\[十/百/10/100\]\[连/l/L\]
        - ~~因为懒得打连字，直接fgo100l不快吗~~
    - 修正是否pickup卡池的检测
- 🚀 v1.02 (2022-07-27)
    - 修正了一部分抽卡结果语句
    - 修正了无pickup四星/五星时的抽卡结果语句
      - 修正了抽卡结果图片
      - 现在抽卡结果为4列
        - 添加了背景，感谢
          [@GWYOG](https://github.com/GWYOG/GWYOG-Hoshino-plugins#8-%E6%88%B3%E6%9C%BA%E5%99%A8%E4%BA%BA%E9%9B%86%E5%8D%A1%E5%B0%8F%E6%B8%B8%E6%88%8Fpokemanpcr)
          的戳一戳集卡插件的背景
        - ~~画个饼，后面拿游戏内截图做十连抽卡的背景（~~
    - 添加了海豹判断条件，当豹跳时发送一张海の翁.jpg
- 🚀 v1.0.1 (2022-07-26)
    - 支持日替池，食用方法：``[切换fgo日替卡池 + 卡池编号 + 日替卡池编号] 切换需要的日替卡池``
- ~~🚀 v1.0.0 (2022-07-26)~~
    - ~~插件上线，暂不支持日替池（在写了在写了）~~

使用方法
======

# 抽卡模拟相关

[fgo十连] fgo抽卡

[fgo百连] 100抽

[获取fgo卡池] 从mooncell获取卡池数据

[查询fgo卡池] 查询本地缓存的卡池以及本群卡池

[切换fgo卡池 + 卡池编号] 切换需要的卡池

[切换fgo日替卡池 + 卡池编号 + 日替卡池编号] 切换需要的日替卡池

# 抽卡管理命令:

[fgo数据初始化] 初始化数据文件及目录，务必安装后先执行此命令！

[fgo数据下载] 下载从者及礼装图标，务必先初始化数据再执行下载！

[跟随最新/剧情卡池] 设置卡池数据更新后跟随最新国服卡池还是国服剧情卡池

[fgo_enable_crt + crt文件路径] 为下载配置crt文件以规避拒绝访问，留空为默认，False为禁用

[fgo_check_crt] 检查本群crt文件配置状态

[设置fgo时间 + 小时 + 分钟 + 秒] 设置自动更新时间间隔，至少输入其中一个参数
- 例如：``设置fgo时间 1小时60分钟60秒``

# 新闻相关：

[获取fgo新闻 + 数量] 从官网获取公告新闻，默认6条，置顶的概率公告会去掉

[查询fgo新闻 + 编号/all] 从本地查询公告具体内容，all代表全部获取

# 数据管理相关
[获取全部从者/礼装/纹章] 获取从者/礼装/纹章的相关内容
- 从者包括职介和指令卡
- 礼装/纹章包括技能

[下载全部卡片资源] 从上述数据中下载对应静态资源
- **※此功能下载的数据并非抽卡模拟器所必须的资源**

安装
======

- 将本项目放在hoshino/modules/目录下
- res目录为抽卡相关素材，需要手动使用指令下载，路径为Hoshino的res/img/fgo文件夹下。
- 使用“fgo数据初始化”“fgo数据下载”“获取fgo卡池”载入卡池数据

说明
======

- ~~暂不支持日替池~~
- 屎代码警告
- ~~部分情况下出金卡的计数会出错（主要是百连），回头有空再修~~
- 官网新闻可能空格过多，晚点写优化
- 全部新闻发送可能导致问题，慎用，相关issue不管
- 推荐初始化顺序：
  - ``fgo数据初始化``
  - ``获取fgo卡池``
  - ``fgo数据下载``
