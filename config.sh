## Version: v2.8.0
## Date: 2021-06-20
## Update Content: 可持续发展纲要\n1. session管理破坏性修改\n2. 配置管理可编辑config下文件\n3. 自定义脚本改为查看脚本\n4. 移除互助相关

## 上面版本号中，如果第2位数字有变化，那么代表增加了新的参数，如果只有第3位数字有变化，仅代表更新了注释，没有增加新的参数，可更新可不更新

## 在运行 ql repo 命令时，是否自动删除失效的脚本与定时任务
AutoDelCron="true"

## 在运行 ql repo 命令时，是否自动增加新的本地定时任务
AutoAddCron="true"

## 拉取脚本时默认的定时规则，当匹配不到定时规则时使用，例如: 0 9 * * *
DefaultCronRule=""

## ql repo命令拉取脚本时需要拉取的文件后缀，直接写文件后缀名即可
RepoFileExtensions="js py ts"

## 由于github仓库拉取较慢，所以会默认添加代理前缀，如不需要请移除
GithubProxyUrl="https://wget.sanling.ml/"

## 设置定时任务执行的超时时间，默认1h，后缀"s"代表秒(默认值), "m"代表分, "h"代表小时, "d"代表天
CommandTimeoutTime="24h"

## 设置批量执行任务时的并发数，默认同时执行5个任务
MaxConcurrentNum="5"

## 在运行 task 命令时，随机延迟启动任务的最大延迟时间
## 默认给javascript任务加随机延迟，如 RandomDelay="300" ，表示任务将在 1-300 秒内随机延迟一个秒数，然后再运行，取消延迟赋值为空
RandomDelay="300"

## 如果你自己会写shell脚本，并且希望在每次运行 ql update 命令时，额外运行你的 shell 脚本，请赋值为 "true"，默认为true
EnableExtraShell="true"

## 是否自动启动bot，默认不启动，设置为true时自动启动，目前需要自行克隆bot仓库所需代码，存到ql/repo目录下，文件夹命名为dockerbot
AutoStartBot=""

## 安装bot依赖时指定pip源，默认使用清华源，如不需要源，设置此参数为空
PipMirror="https://pypi.tuna.tsinghua.edu.cn/simple"

## 通知环境变量
## 1. Server酱
## https://sct.ftqq.com
## 下方填写 SCHKEY 值或 SendKey 值
export PUSH_KEY=""

## 2. BARK
## 下方填写app提供的设备码，例如：https://api.day.app/123 那么此处的设备码就是123
export BARK_PUSH=""
## 下方填写推送声音设置，例如choo，具体值请在bark-推送铃声-查看所有铃声
export BARK_SOUND=""
## 下方填写推送消息分组，默认为"QingLong"
export BARK_GROUP="QingLong"

## 3. Telegram 
## 下方填写自己申请@BotFather的Token，如10xxx4:AAFcqxxxxgER5uw
export TG_BOT_TOKEN=""
## 下方填写 @getuseridbot 中获取到的纯数字ID
export TG_USER_ID=""
## Telegram 代理IP（选填）
## 下方填写代理IP地址，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "127.0.0.1"
## 如需使用，请自行解除下一行的注释
export TG_PROXY_HOST=""
## Telegram 代理端口（选填）
## 下方填写代理端口号，代理类型为 http，比如您代理是 http://127.0.0.1:1080，则填写 "1080"
## 如需使用，请自行解除下一行的注释
export TG_PROXY_PORT=""
## Telegram 代理的认证参数（选填）
export TG_PROXY_AUTH=""
## Telegram api自建反向代理地址（选填）
## 教程：https://www.hostloc.com/thread-805441-1-1.html
## 如反向代理地址 http://aaa.bbb.ccc 则填写 aaa.bbb.ccc
## 如需使用，请赋值代理地址链接，并自行解除下一行的注释
export TG_API_HOST=""

## 4. 钉钉 
## 官方文档：https://developers.dingtalk.com/document/app/custom-robot-access
## 下方填写token后面的内容，只需 https://oapi.dingtalk.com/robot/send?access_token=XXX 等于=符号后面的XXX即可
export DD_BOT_TOKEN=""
export DD_BOT_SECRET=""

## 5. 企业微信机器人
## 官方说明文档：https://work.weixin.qq.com/api/doc/90000/90136/91770
## 下方填写密钥，企业微信推送 webhook 后面的 key
export QYWX_KEY=""

## 6. 企业微信应用
## 参考文档：http://note.youdao.com/s/HMiudGkb
## 下方填写素材库图片id（corpid,corpsecret,touser,agentid），素材库图片填0为图文消息, 填1为纯文本消息
export QYWX_AM=""

## 7. iGot聚合
## 参考文档：https://wahao.github.io/Bark-MP-helper
## 下方填写iGot的推送key，支持多方式推送，确保消息可达
export IGOT_PUSH_KEY=""

## 8. Push Plus
## 官方网站：http://www.pushplus.plus
## 下方填写您的Token，微信扫码登录后一对一推送或一对多推送下面的token，只填 PUSH_PLUS_TOKEN 默认为一对一推送
export PUSH_PLUS_TOKEN=""
## 一对一多推送（选填）
## 下方填写您的一对多推送的 "群组编码" ，（一对多推送下面->您的群组(如无则新建)->群组编码）
## 1. 需订阅者扫描二维码 2、如果您是创建群组所属人，也需点击“查看二维码”扫描绑定，否则不能接受群组消息推送
export PUSH_PLUS_USER=""

## 9. go-cqhttp
## gobot_url 推送到个人QQ: http://127.0.0.1/send_private_msg  群：http://127.0.0.1/send_group_msg 
## gobot_token 填写在go-cqhttp文件设置的访问密钥
## gobot_qq 如果GOBOT_URL设置 /send_private_msg 则需要填入 user_id=个人QQ 相反如果是 /send_group_msg 则需要填入 group_id=QQ群 
## go-cqhttp相关API https://docs.go-cqhttp.org/api
export GOBOT_URL=""
export GOBOT_TOKEN=""
export GOBOT_QQ=""

## 10. gotify
## gotify_url 填写gotify地址,如https://push.example.de:8080
## gotify_token 填写gotify的消息应用token
## gotify_priority 填写推送消息优先级,默认为0
export GOTIFY_URL="";
export GOTIFY_TOKEN="";
export GOTIFY_PRIORITY=0;

## 其他需要的变量，脚本中需要的变量使用 export 变量名= 声明即可
export DPQDTK=""


## 佳孚（YARDFORCE）京东自营旗舰店  ★ 豆豆加购 ★

## 加购有礼-m_jd_wx_addCart.js
export M_WX_ADD_CART_URL="https://lzkj-isv.isvjcloud.com/wxCollectionActivity/activity2/1aeedfe463e9461fa8e698dbc11f5797?activityId=1aeedfe463e9461fa8e698dbc11f5797"


export M_WX_LUCK_DRAW_URL="https://lzkj-isv.isvjcloud.com/miniProgramShareInfo/getInfo?activityId=713f3d5b2db14921b356ad5b4013c91b"

export guaopencard150="true"
export guaopencard_addSku150="true"



export WP_APP_TOKEN_ONE="AT_bCs2NsNUCNNHP9zfh5ViUsAXPjsu6Yih"

##游戏通用-jd_game.js
## 通用游戏-jd_game.js
export WXGAME_ACT_ID="101c3c1443f64c86937614825ba6ae6d"

## 读秒拼手速-jd_wxSecond.js
export jd_wxSecond_activityId="9bef59aad10e44a5994933672e22aa85"




export JD_19E="true"

## 超级店铺签到 jd_sevenDay.js
export SEVENDAY_LIST="b78817d3730b48188380914df178c30c"








## 集卡抽奖-jd_wxCollectCard.js

export jd_wxCollectCard_activityId="e794d514288249b4a9eeafbcc7d6dc6a"

## CJ组队瓜分-jd_cjzdgf.js
#export jd_cjhy_activityId="4f6389560b2749ae81b2abc91f4ddf23"
export jd_cjhy_activityUrl="https://cjhydz-isv.isvjcloud.com"
export jd_cjhy_activityId="424aa0051abc4e88b7b1f8dbe24a6cac"

## 超级店铺签到 jd_sevenDay.js

export SEVENDAY_LIST="d3efee22ea1549d998064aba8049b059"

##JOY通用开卡活动-jd_joyopen.js
##export JD_JOYOPEN="70315892a06d4c5fa4061af1eaef9d90"

##JOY通用开卡活动-jd_joyopen.js
export JD_JOYOPEN="11f663b79e7c48c08cc6b93cd61b0825"
##通用抽奖机-jd_Lottery.js
export JD_Lottery="f86c818ff35549bd9e9d68acdafb8ebf"

export SEVENDAY_LIST2="ac8509337249496f8cadfa43c2fc20f6","8af4ada957f14cb38b4e9d7954d14755"

export PZ="PKASTT01596I2L3HPZsoBs4QCTdWmYaRzTcjeQOc"

## LZ分享有礼-jd_jd_share.js
export jd_fxyl_activityId="3606435cda984aca83484628e827cab2"






jd_zdjr_activityId="bb8c51279e9842a2bd77f2ee2e3d52fd"

## 微定制组队瓜分-jd_team60.js
export jd_wdz_activityId="d5ac35f5ac8a4b2c96a85de908c87edd"
export jd_wdz_activityUrl="https://cjhydz-isv.isvjcloud.com"

export CODE618="lII0LBC"  


export guaopencard174="true" 
export guaopencard_addSku174="true"
export guaopencard_draw174="3"

## 大牌开卡
export opencard_toShop="true"
#export DPLHTY="fd50e092e2384fb7adc6ff0_220602"
#export DPLHTY="48111057c5714efcbbe5f58b6_220605"
#export DPLHTY="89b32721908044869_220606"


export DPLHTY="b4becfdc96c04478b_220701"

# M加购
export M_API_TOKEN="1880637003:7e19fcba3514a34de83735af711ffd8a"
export M_FOLLOW_SHOP_ARGV="11608735_11886992"

## LZ购物车锦鲤-jd_wxCartKoi.js
export jd_wxCartKoi_activityId="e2d270732dc54ec689caae18c222c82d"

## 入会开卡领取礼-jd_OpenCard_Force.js
## 入会开卡领取礼-jd_OpenCard_Force.js
export VENDER_ID="1000003263&1000411104&1000361242"


export enabled="true"
export OPENCARD_BEAN="0"


## LZ刮刮乐抽奖-jd_drawCenter.js
export jd_drawCenter_activityId="61d3b8c3b7c04d8398cb82e57175328d"

## PKC关注有礼-特效
export PKC_TXGZYL="e1f24b4436e048ca855df1b838bcd7ba"

## LZ粉丝互动-jd_wxFansInterActionActivity.js
export jd_wxFansInterActionActivity_activityId="d624be359a5a4c53970729f1ae865e55"
export jd_wxShopFollowActivity_activityId="1882bbe81bb84ae8be2002cad998760c"

## 邀好友赢大礼-jd_yqhy.py
export yhyactivityId="dVF7gQUVKyUcuSsVhuya5d2XD4F"
export yhyauthorCode="7a6ccc8813464ba8a72ae90037840ac0"
export yhypin="jd_QGISuMhWHFxK"  

# 测试  2
