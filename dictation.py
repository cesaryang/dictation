from gtts import gTTS
import os
import random
import time
import pygame  # 新增
import sys

def speak_word(word, lang='en'):
    """将单词转换为语音并播放"""
    try:
        tts = gTTS(text=word, lang=lang, slow=False)
        filename = "temp_word.mp3"
        tts.save(filename)
        pygame.mixer.init()
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)
        # 卸载音乐，确保文件释放
        pygame.mixer.music.unload()
        try:
            os.remove(filename)
        except Exception as e:
            print(f"删除音频文件失败: {e}")
    except Exception as e:
        print(f"播放音频时出错: {e}")
        print(f"请确保您的网络连接正常，或尝试安装必要的音频播放器。")

def load_words(filename="words.txt"):
    """从文件中加载单词列表"""
    words = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                word = line.strip().lower()
                if word:  # 跳过空行
                    words.append(word)
    except FileNotFoundError:
        print(f"错误: 文件 '{filename}' 未找到。请创建包含单词的文件。")
    return words

def main():
    words = load_words("words.txt")
    if not words:
        return
    random.shuffle(words)
    total = 0
    correct = 0
    for word in words:
        print("正在播放单词...")
        speak_word(word)
        user_input = input("请输入你听到的单词（q 退出）：").strip().lower()
        if user_input in ('q', 'exit'):
            print("已退出背词。")
            break
        total += 1
        if user_input == word:
            correct += 1
            print("\033[32m正确！\033[0m\n")  # 绿色输出
        else:
            print(f"\033[31m错误\033[0m，正确拼写是：{word}\n")
    print(f"\n本次共背词 {total} 个，正确 {correct} 个。")

if __name__ == "__main__":
    main()