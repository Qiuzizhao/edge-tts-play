import edge_tts
import pygame

def tts(TEXT):
    """Main function"""     
    # TEXT = "你好哟，智能语音助手小伊"
    VOICE = "zh-CN-XiaoyiNeural"
    OUTPUT_FILE = "output.mp3"
    
    communicate = edge_tts.Communicate(TEXT, VOICE)
    communicate.save_sync(OUTPUT_FILE)
    
 
    # 初始化pygame
    pygame.init()
 
    # 创建音乐播放器对象
    pygame.mixer.init()
 
    # 加载mp3文件
    pygame.mixer.music.load(OUTPUT_FILE)
 
    # 播放音乐
    pygame.mixer.music.play()
    
    # 等待音乐播放完毕
    while pygame.mixer.music.get_busy():
        continue
 
    # 停止音乐
    pygame.mixer.music.stop()
    
    # 删除mixer对象
    pygame.mixer.quit()
    
    # 删除临时文件
#    os.remove(OUTPUT_FILE)


if __name__ == "__main__":
    while True:
        user_input = input("\n请输入：")
        tts(user_input)
