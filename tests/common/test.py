import asyncio
import edge_tts

async def main():
    text = "你是我的朋友吗？"  # 任意中文都行
    voice = "zh-CN-XiaoxiaoNeural"  # 微软童声
    output_path = "child_voice.mp3"

    ssml = f'''
    <speak version="1.0" xml:lang="zh-CN">
        <voice name="{voice}">
            <prosody rate="x-slow" pitch="+8st">
                {text}
            </prosody>
        </voice>
    </speak>
    '''

    communicate = edge_tts.Communicate(ssml)
    await communicate.save(output_path)
    print(f"✅ 成功生成语音：{output_path}")

asyncio.run(main())
