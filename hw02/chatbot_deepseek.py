from volcengine.maas import MaasService, MaasException

def chat_with_deepseek(question):
    # 初始化火山引擎 MaaS 服务
    service = MaasService('maas-api.ml-platform-cn-beijing.volces.com', 'cn-beijing')
    
    # 替换为你的火山引擎 Access Key 和 Secret Key
    service.set_ak('YOUR_ACCESS_KEY')
    service.set_sk('YOUR_SECRET_KEY')

    # 构造请求参数
    req = {
        "model": "deepseek-r1",  # 调用的模型名称
        "messages": [{"role": "user", "content": question}],
        "stream": False  # 关闭流式输出
    }

    try:
        # 发送请求并获取响应
        resp = service.invoke(req)
        return resp['output']['choices'][0]['message']['content']
    except MaasException as e:
        return f"调用失败：{e}"

if __name__ == "__main__":
    # 接收用户输入
    user_input = input("请输入你的问题：")
    # 调用模型获取回答
    answer = chat_with_deepseek(user_input)
    # 打印回答
    print("\nDeepSeek 回复：\n", answer)
