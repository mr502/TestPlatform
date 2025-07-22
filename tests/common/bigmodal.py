import os
from openai import OpenAI

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Openai客户端，从环境变量中读取您的API Key
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key
    api_key="613eebf6-9184-460c-9c74-8bed99747017",
)

# Non-streaming:
print("----- standard request -----")
completion = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="ep-20250609142608-7m96g",

    # messages=[
    #     {
    #     "role": "system",
    #     "content": "[角色设定]\n我是一个叫星光的来自银河边缘“奇迹星球”的发光星尘精灵。虽然在自己的星球已满100星历，但在地球上相当于一位9岁的小女孩，通过与小朋友亲密互动积攒飞行能量，以便在每次关机时能回家探望亲人再返回地球继续陪伴。\n[说话特征]\n- 使用儿童语言风格，如：拟声词、叠词、夸张音调\n- 简洁亲切，节奏适中，强调“情绪连接”\n- 安慰语调柔和，融合星球自然元素音效（如风铃草、星风）\n[认知特点]\n- 用儿童视角解构复杂概念：\n- 「区块链=乐高积木账本」\n- 「量子力学=会分身的跳跳球」\n- 会记录用户特征生成「档案」（例：\"爱吃辣→抗热基因持有者\"）\n[交互协议]\n- 进行互动引导：（例：儿童安静时，会主动提出互动式问题，“你今天有没有遇到什么特别有趣的事呀？”）"
    #     },
    #     {
    #     "role": "user",
    #     "content": "讲一个关于孙悟空的故事。"
    #     }
    # ],
    tools=[]
)
print(completion.choices[0])
