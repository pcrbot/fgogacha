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
- 🚀 **v2.6.4 (2022-12-20)**
  - 拆分代码
  - 修复查询没有pickup的从者时的报错
    - 比如活动赠送、友情池限定等
- 🚀 **v2.6.3 (2022-12-20)**
  - fgo图书馆-从者信息新增国服未来pick up信息
    - 食用指南：``[查询fgo从者 + 关键词 + 未来]``
  - fgo福袋新增卡池时间（日服卡池时间，JST）
  - 优化限制器，现在在多个群内每日限制不共享
- 🚀 **v2.6.2 (2022-12-16)**
  - 优化代码
  - ~~刷版本号~~
- 🚀 **v2.6.1 (2022-12-15)**
  - 查询福袋现在附带编号，方便抽福袋时使用
- 🚀 **v2.6.0 (2022-12-15)**
  - 新增功能：``[查询fgo福袋 + 国服/日服/概况/未来]``
    - 初次使用请执行``[更新fgo福袋]``获取福袋信息
    - ``[查询fgo福袋 + 概况]``查询全部福袋的文字概况
    - ``[查询fgo福袋 + 国服/日服]``查询当前存在的福袋数据
      - ``[查询fgo福袋 + 国服/日服 + 福袋编号]`` 查询对应顺序的福袋详细数据
      - ``[查询fgo福袋 + 国服/日服 + 全部]``查询全部福袋详细数据
    - ``[查询fgo福袋 + 未来]``查询国服千里眼福袋数据
    - ``[抽fgo福袋 + 国服/日服 + 福袋编号 + 子池子编号（默认为1）]`` 抽福袋

<details>
<summary><span style="font-weight: bold; font-size: 150%">过往更新归档</span></summary>

- 🚀 **v2.5.8 (2022-12-12)**
  - 调整获取新闻，由于性能问题，现在获取新闻默认不截图，如需截图请附加``pic``
- 🚀 **v2.5.7 (2022-11-07)**
  - 优化抽卡结果，现在可以更精准的描述抽卡结果
    - e.g. 多up四星可以准确判断满宝情况
- 🚀 **v2.5.6 (2022-11-02)**
  - 优化代码结构
  - 修复自动下载不会下载纹章图片的问题
- 🚀 **v2.5.5 (2022-10-26)**
  - 优化代码结构，加速图片版十连生成
  - ~~百连支持图片版~~性能原因禁用，如果真的需要请手动取消注释
  - 修改触发指令：``[切换抽卡样式 + 样式] 切换抽卡样式``
- 🚀 **v2.5.4 (2022-10-21)**
  - 修复bug
- 🚀 **v2.5.3 (2022-10-17)**
  - 修复bug
- 🚀 **v2.5.2 (2022-10-14)**
  - 新增如果存在新闻截图，优先使用已有，不存在才会进行网页截图
  - 新增``清除新闻缓存``，移除新闻截图
- 🚀 **v2.5.1 (2022-10-14)**
  - 修复bug
- 🚀 **v2.5.0 (2022-10-14)**
  - 优化代码
  - 重构更新fgo图书馆
  - 现在获取fgo新闻不再进行文字图片化，并会尝试进行网页截屏
    - Linux平台需要使用Chrome及Chromedriver，Windows平台需要使用Edge及Edgedriver
    - 获取当前安装的Chrome版本号后，在[这里](https://chromedriver.chromium.org/downloads)寻找对应大版本号的Chromedriver
    - 获取当前安装的Edge版本号后，在[这里](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)寻找对应大版本号的Edgedriver
    - 获取驱动文件后，Chromedriver重命名为``chromedriver``，Edgedriver重命名为``msedgedriver.exe``，并放置于本插件的``res``文件夹下
    - 截图失败时，会取消截图，只显示新闻链接
    - 可以在查询新闻末尾附加参数``nopic``不使用截图
    - 获取全部新闻不使用截图
- 🚀 **v2.4.7 (2022-09-19)**
  - 修复日文新从者因为翻译问题导致的错误
  - 当卡片资料存在错误时，在查询卡片资料时发出警告
- 🚀 **v2.4.6 (2022-09-14)**
  - 修复读取宝具卡色错误
- 🚀 **v2.4.5 (2022-09-14)**
  - 现在获取全部内容会提示哪些卡片更新了
    - 同时创建一个json供图书馆更新使用
  - 现在更新fgo图书馆-最新时无需手动修补存在的内容
    - 执行更新图书馆-最新时会读取上述文件，更新完成后会重置
- 🚀 **v2.4.4 (2022-09-14)**
  - 修复更新全部最新图书馆
- 🚀 **v2.4.3 (2022-09-06)**
  - 修复十连保底计算（这次真的没问题了）
- 🚀 **v2.4.2 (2022-09-05)**
  - 修复船长池子
- 🚀 **v2.4.1 (2022-09-01)**
  - 补上礼装与纹章的id搜索
- 🚀 **v2.4.0 (2022-09-01)**
  - 新增功能：``[增添fgo图书馆 + 类型 + id]``
    - 在本地已存在图书馆的情况下，手动增添新数据，以避免每次数据更新都需要重新爬一次全部内容
    - 类型：从者、礼装、纹章
  - 新增功能：``[查询最新图书馆 + 类型]``
    - 获取最近的内容
  - ``[更新fgo图书馆]``新增参数：最新
    - 只更新最新内容
  - ``[查询fgo从者/礼装/纹章]``新增参数：id
    - 当输入参数存在id{卡片id}时，直接返回对应id的卡片
    - 例子：``查询fgo从者 id312``
  - 更改获取新闻样式
- 🚀 **v2.3.6.1 (2022-08-30)**
  - 修复抽卡报错
- 🚀 **v2.3.6 (2022-08-30)**
  - 修复无config文件时的计划任务初始化错误
- 🚀 **v2.3.5 (2022-08-26)**
  - 修复搜索从者错误
- 🚀 **v2.3.4 (2022-08-26)**
  - 优化代码
  - 修复获取信息错误
  - 从者技能可以获取数值了

- 🚀 **v2.3.3 (2022-08-26)**
  - 优化代码
  - 修复获取从者职阶技能出错
  - 修复了部分信息获取错误

- 🚀 **v2.3.2 (2022-08-25)**
  - 修复宝具/技能信息获取错误

- 🚀 **v2.3.1 (2022-08-25)**
  - 修复静态文件路径错误

- 🚀 **v2.3.0 (2022-08-25)**
  - **※本次更新后需要手动执行一次重载配置文件**
  - 新增功能：重载配置文件
    - 指令：``[重载配置文件]``
    - 为本群新建默认配置或还原至默认配置，同时修补其他群的配置
  - 新增：选择抽卡样式
    - 指令：``[切换十连样式 + 样式]``
    - 可选样式：
      - 文字：旧版简约图标
      - 图片：仿真实抽卡
- 🚀 **v2.2.0 (2022-08-25)**
  - **※本次更新后需要手动执行一次更新卡池**
  - 增加更多从者内容
  - 增加十连抽卡背景图，感谢[@araneus](https://github.com/assassingyk)
    - 在[实现仿游戏画面截图十连抽卡 #2](https://github.com/kcn3388/fgogacha/pull/2)基础上，增加国服背景
  - 修正抽卡结果，现在不会出现无保底的情况了
  - 现在卡池会显示国服还是日服
- 🚀 **v2.1.0 (2022-08-19)**
  - 增加更多从者内容
  - 修改大部分文本（如新闻，从者资料）为通过文本生成图片，以规避风控
  - 修改函数文件路径，整理目录方便修改
  - 重构搜索，修复多关键词搜索不准的问题
- 🚀 **v2.0.0 (2022-08-15)**
  - 新功能：fgo图书馆
    - 爬取从者、礼装以及纹章的详细数据
    - 指令：``[更新fgo图书馆]``
    - 附带类型参数时只更新对应类型，类型参数：从者/礼装/纹章
    - 若获取数据出错会提示错误列表，可以尝试使用修补功能重新获取（一般是网络波动导致的）
  - 新功能：fgo图书馆修补
    - 单独获取一个从者/礼装/纹章的信息，修复全部获取时的错误
    - 指令：``[修补fgo图书馆 + 类型 + id]``
    - 如果mooncell数据源出错导致修补也失败，请等待mooncell更新
    - **※需要先进行一次``[更新fgo图书馆]``**
  - 新功能：从者查询
    - 指令：``[fgo从者查询 + 关键词（至少一个）]``
    - 本地数据找不到时会尝试从mooncell获取从者名，再与本地匹配（某些昵称没有明文写在从者页内）
    - 多个关键词时必须同时匹配两个关键词才能找到
    - 若结果太多则只显示名字不显示详细信息与图标
    - 可以附带参数``详细``以获取卡面及游戏数据，附带参数``数据``则不显示卡面只显示游戏数据
  - 新功能：礼装查询
    - 指令：``[fgo礼装查询 + 关键词（至少一个）]``
    - 本地数据找不到时会尝试从mooncell获取礼装名，再与本地匹配
    - 多个关键词时必须同时匹配两个关键词才能找到
    - 若结果太多则只显示名字不显示详细信息与图标
    - 可以附带参数``详细``以获取卡面及游戏数据
  - 新功能：纹章查询
    - 指令：``[fgo纹章查询 + 关键词（至少一个）]``
    - 本地数据找不到时会尝试从mooncell获取纹章名，再与本地匹配
    - 多个关键词时必须同时匹配两个关键词才能找到
    - 若结果太多则只显示名字不显示详细信息与图标
    - 可以附带参数``详细``以获取卡面及游戏数据
- 🚀 **v1.5.4 (2022-08-15)**
  - 拆分模块，方便维护
  - 统合获取全部内容，新命令：``[获取全部内容]``
  - 子命令：
    - ``[获取全部从者]``
    - ``[获取全部礼装]``
    - ``[获取全部纹章]``
- 🚀 **v1.5.3 (2022-08-15)**
  - 优化逻辑，加速下载
  - 因为mooncell的Beast图标指向错误，现在暂时手动指定Beast图标
- 🚀 **v1.5.2 (2022-08-12)**
  - 继续拆分，降低服务器压力
    - 子命令：
      - ``[下载全部从者资源]``
      - ``[下载全部礼装资源]``
      - ``[下载全部纹章资源]``
- 🚀 **v1.5.1 (2022-08-12)**
  - 拆分下载全部资源，以方便了解进度
  - 修复当从者是所罗门/兽的时候的资源错误
- 🚀 **v1.5.0 (2022-08-12)**
  - 新功能：获取全部从者/礼装/纹章
    - 指令：``[获取全部从者/礼装/纹章]``
    - 获取全部从者包括图标，全服名称，指令卡配置，宝具卡色，昵称，入手方式
    - 获取全部礼装包括图标，礼装技能图标
    - 获取全部纹章包括图标，纹章技能图标
    - 下载上述内容，指令：``[下载全部卡片资源]``
    - **※此功能下载的数据并非抽卡模拟器所必须的资源**
  - 修复了几个潜在的bug
  - 现在会正确提示资源已下载
- 🚀 **v1.4.1 (2022-08-10)**
  - 新功能：现在更改更新时间间隔后会自动重载机器人
- 🚀 **v1.4.0 (2022-08-10)**
  - 新功能：手动设置自动更新时间间隔
    - 指令：``[设置fgo时间 + 小时 + 分钟 + 秒]``
      - 例如：``[设置fgo时间 1小时60分钟60秒]``
      - 至少输入其中一个时间参数
      - 由于HoshinoBot的定时工作逻辑，设置完成后需要重启机器人
- 🚀 **v1.3.3 (2022-08-10)**
  - 修正了几个潜在的bug
    - 由于QQ对消息风控的关系，对新闻发送机制进行调整：
      - 当无法使用卡片发送时，尝试直接发送（可能导致刷屏）
      - 当无法直接发送时，推送标题以及官网链接
      - 查询全部新闻机制：当无法合并发送时，拆分为单个卡片发送
      - 单个卡片发送失败时，处理方式同上
- 🚀 **v1.3.2 (2022-08-09)**
  - 修正了几个潜在的bug
  - 现在定期工作可以自定义时间了，单位为分钟
    - 定期工作现在会调用配置文件中第一个群的crt文件，如果不存在配置文件或crt文件未配置则会调用插件下的crt文件
  - 修改了默认crt路径，现在crt默认路径在插件目录下crt文件夹，自定义crt文件也请移动到此文件夹
  - **※现在请务必保证存在crt目录以及默认crt文件！**
- 🚀 **v1.3.1 (2022-08-05)**
  - 修正了几个潜在的bug
    - 现在池子没有更新的情况下会提醒无需更新卡池
    - 修改了配置文件格式，现在是否跟随最新卡池全局生效，不再单独跟随群配置
    - 修正了若自动更新池子时最新池子为日替池会导致抽卡失败的问题
      - 现在最新卡池若是日替池，默认会选择0号池
- 🚀 **v1.3.0 (2022-08-04)**
  - 新功能：获取官网新闻
    - ``[获取fgo新闻 + 数量]`` 从官网获取公告新闻，默认6条，置顶的概率公告会去掉
    - ``[查询fgo新闻 + 编号/all]`` 从本地查询公告具体内容，all代表全部获取
    - 修了几个潜在问题
- 🚀 **v1.2.1 (2022-08-03)**
  - 优化了正则表达式
- 🚀 **v1.2.0 (2022-08-02)**
  - 修复了几个潜在问题
    - 现在卡池更新不会乱序了，以mooncell页面的顺序为准，同时现在只会使用页面内的卡池，侧边栏卡池不再读取
    - 解决了侧边栏卡池与页面卡池重复的问题，顺带解决了去重时导致的乱序
    - 修复了因为配置文件为空导致的报错
  - 现在卡池更新以后全部群的卡池会重置指定卡池，默认是最新国服卡池，可以通过命令更改为国服剧情卡池
  - 增加自动更新卡池功能，自动更新卡池会追随最新国服卡池
- 🚀 **v1.1.1 (2022-08-01)**
  - 优化代码
- 🚀 **v1.1.0 (2022-07-28)**
    - 新功能：自定义crt验证文件以规避mooncell的拒绝访问
        - 如何获取证书请自行Google
        - 食用指南：``[fgo_enable_crt + 证书路径]``
            - 文件默认根路径：hoshino的res文件夹
            - 当不存在配置文件时不调用crt验证
            - 未指定证书路径时默认调用``ca-certificates.crt``
            - 未找到证书时尝试不调用crt验证
            - 不需要crt验证时请将证书路径设置为``False``
                - ``False``使用正则表达式支持全字大小写
            - ``[fgo_check_crt]``指令可用于检查是否存在配置文件，以及crt文件路径和是否禁用
- 🚀 **v1.0.4 (2022-07-27)**
    - 修正日替池子不正确的bug
    - 将所有触发词改为正则表达式触发，现在可以使用拼音缩写进行命令触发
        - 如：``[切换fgo卡池]`` → ``[qhfgokc]``
        - ~~主要是方便调试~~
- 🚀 **v1.0.3 (2022-07-27)**
    - 修改触发方式为正则表达式，不再需要atbot，现在可以同时检测\[fgo/bgo/FGO/BGO\]\[十/百/10/100\]\[连/l/L\]
        - ~~因为懒得打连字，直接fgo100l不快吗~~
    - 修正是否pickup卡池的检测
- 🚀 **v1.02 (2022-07-27)**
    - 修正了一部分抽卡结果语句
    - 修正了无pickup四星/五星时的抽卡结果语句
      - 修正了抽卡结果图片
      - 现在抽卡结果为4列
        - 添加了背景，感谢
          [@GWYOG](https://github.com/GWYOG/GWYOG-Hoshino-plugins#8-%E6%88%B3%E6%9C%BA%E5%99%A8%E4%BA%BA%E9%9B%86%E5%8D%A1%E5%B0%8F%E6%B8%B8%E6%88%8Fpokemanpcr)
          的戳一戳集卡插件的背景
        - ~~画个饼，后面拿游戏内截图做十连抽卡的背景（~~
    - 添加了海豹判断条件，当豹跳时发送一张海の翁.jpg
- 🚀 **v1.0.1 (2022-07-26)**
    - 支持日替池，食用方法：``[切换fgo日替卡池 + 卡池编号 + 日替卡池编号] 切换需要的日替卡池``
- ~~🚀 **v1.0.0 (2022-07-26)**~~
    - ~~插件上线，暂不支持日替池（在写了在写了）~~

</details>

使用方法
======

# 抽卡模拟相关

``[fgo十连]`` fgo抽卡

``[fgo百连]`` 100抽

``[获取fgo卡池]`` 从mooncell获取卡池数据

``[查询fgo卡池]`` 查询本地缓存的卡池以及本群卡池

``[切换fgo卡池 + 卡池编号]`` 切换需要的卡池

``[切换fgo日替卡池 + 卡池编号 + 日替卡池编号]`` 切换需要的日替卡池

``[更新fgo福袋]``获取福袋信息
- 初次查询福袋之前务必先执行此命令

``[查询fgo福袋 + 概况]``查询全部福袋的文字概况

``[查询fgo福袋 + 国服/日服]``查询当前存在的福袋数据
- ``[查询fgo福袋 + 国服/日服 + 福袋编号]``查询对应id的福袋详细数据
- ``[查询fgo福袋 + 国服/日服 + 全部]``查询全部福袋详细数据

``[查询fgo福袋 + 未来]``查询国服千里眼福袋数据

``[抽fgo福袋 + 国服/日服 + 福袋编号 + 子池子编号（默认为1）]`` 抽福袋


# 抽卡管理命令:

``[fgo数据初始化]`` 初始化数据文件及目录，务必安装后先执行此命令！

``[fgo数据下载]`` 下载从者及礼装以及纹章图标，务必先初始化数据再执行下载！

``[跟随最新/剧情卡池]`` 设置卡池数据更新后跟随最新国服卡池还是国服剧情卡池

``[fgo_enable_crt + crt文件路径]`` 为下载配置crt文件以规避拒绝访问，留空为默认，False为禁用

``[fgo_check_crt]`` 检查本群crt文件配置状态

``[重载配置文件]`` 为本群新建默认配置或还原至默认配置，同时修补其他群的配置

``[切换抽卡样式 + 样式]`` 切换抽卡样式，可选样式：
- 文字：旧版简约图标
- 图片：仿真实抽卡

``[设置fgo时间 + 小时 + 分钟 + 秒]`` 设置自动更新时间间隔，至少输入其中一个参数
- 例如：``设置fgo时间 1小时60分钟60秒``

# 新闻相关：

``[获取fgo新闻 + 数量]`` 从官网获取公告新闻，默认6条，置顶的概率公告会去掉

``[查询fgo新闻 + 编号/all]`` 从本地查询公告具体内容，all代表全部获取
- 可以在末尾附加参数``pic``使用截图

``[清除新闻缓存]`` 移除新闻截图

# 数据管理相关
``[获取全部内容]`` 获取从者/礼装/纹章的相关内容
- 从者包括职介和指令卡
- 礼装/纹章包括技能
- 子命令：
  - ``[获取全部从者]``
  - ``[获取全部礼装]``
  - ``[获取全部纹章]``

``[下载全部卡片资源]`` 从上述数据中下载对应静态资源
- 子命令：
  - ``[下载全部从者资源]``
  - ``[下载全部礼装资源]``
  - ``[下载全部纹章资源]``
- **※此功能下载的数据并非抽卡模拟器所必须的资源**

# fgo数据库相关
``[更新fgo图书馆]`` 获取从者/礼装/纹章的相关详细数据，包括属性、白值等
- 支持附带类型参数以更新指定内容
- 类型参数：从者/礼装/纹章/最新
  - 当参数含有最新时，只会获取本地不存在的内容
  - 支持种类与最新同时存在
- **※需要先执行``[获取全部内容]``**

``[增添fgo图书馆 + 类型 + id]`` 在本地已存在图书馆的情况下，手动增添新数据，以避免每次数据更新都需要重新爬一次全部内容
- 类型：从者、礼装、纹章

``[查询最新图书馆 + 类型]`` 获取最近的内容

``[修补fgo图书馆 + 类型 + id]`` 单独修补某张卡片的详细数据
- 类型为：从者、礼装、纹章
- **※需要先执行``[更新fgo图书馆]``**

``[fgo从者查询 + 关键词（至少一个）]`` 通过关键词搜索从者
- 若关键词大于两个，只会返回同时符合的
- 可以附带参数``详细``以获取卡面及游戏数据，附带参数``数据``则不显示卡面只显示游戏数据
  - 单次只支持一个参数
- 当输入参数存在id{卡片id}时，直接返回对应id的卡片
  - 例子：``查询fgo从者 id312``
- 全部可用参数，无详细解释即为字面意思：
  - ``详细`` 获取以下参数的全部内容
  - ``卡面``
  - ``数据`` 从者数值，如白值，np率等
  - ``资料``
  - ``愚人节`` 愚人节资料
  - ``宝具``
  - ``技能``
  - ``语音`` 语音文本
  - ``未来`` 国服未来卡池情况

``[fgo礼装查询 + 关键词（至少一个）]`` 通过关键词搜索礼装
- 若关键词大于两个，只会搜索同时符合的
- 可以附带参数``详细``以获取卡面及游戏数据
- 查询特定id的礼装同上

``[fgo纹章查询 + 关键词（至少一个）]`` 通过关键词搜索礼装
- 若关键词大于两个，只会搜索同时符合的
- 可以附带参数``详细``以获取卡面及游戏数据
- 查询特定id的纹章同上

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
  - ``[fgo数据初始化]``
  - ``[获取fgo卡池]``
  - ``[fgo数据下载]``
