import os
os.environ["PYTHONIOENCODING"] = "utf-8"
import whisper

# 加载 Whisper base 模型
model = whisper.load_model("base")

# 识别当前目录下的视频文件（文件名已确认是 leo_20260326.mp4）
result = model.transcribe("leo_20260326.mp4")

# 打印识别结果
print("识别结果：\n", result["text"])

# 将结果保存到 hw04 目录下的 transcribe_result.txt
with open("../transcribe_result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])