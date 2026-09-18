import sys
import time
import pygame
from rich.console import Console
from rich.text import Text

console = Console()

pygame.mixer.init()
pygame.mixer.music.load("company.mp3")


def print_lyrics(loop: bool = True):
    lines = [
        "🎵 [music intro]",
        "can we, we keep, keep each other company?",
        "maybe we, can be, be each other's company",
        "oh company",
        "let's end each other's lonely nights",
        "be each other's paradise",
        "need a picture for my frame",
        "someone to share my reign",
        "tell me what you wanna drink",
        "i'll tell you what i got in mind",
        "oh, i don't know your name",
        "but i feel like that's gonna change",
        "you ain't gotta be my lover",
        "for you to call me baby",
        "never been about no pressure",
        "ain't that serious?",
        "can we, we keep, keep each other company?",
        "maybe we, can be, be each other's company",
        "oh company",
        "it ain't about the complications",
        "i'm all about the elevation",
        "we can keep it goin' up",
        "oh, don't miss out on us",
        "just wanna have a conversation",
        "forget about the obligations",
        "maybe we can stay in touch",
        "oh, that ain't doin' too much",
        "you ain't gotta be my lover for me to call you baby",
        "never been about no pressure, ain't that serious?",
        "can we, we keep, keep each other company?",
        "maybe we, can be, be each other's company",
        "oh company"
    ]

    timestamps = [
        0.0,   
        2.1,   
        12.0,  
        20.0,  
        22.5,  
        25.0,  
        27.5,  
        30.0,  
        32.5,  
        35.0,  
        37.5,  
        40.0,  
        42.5,  
        45.0,  
        47.5,  
        50.0,  
        52.5,  
        62.0,  
        70.0,  
        74.0,  
        76.5,  
        79.0,  
        81.5,  
        84.0,  
        86.5,  
        89.0,  
        91.5,  
        94.0,  
        98.0,  
        102.0, 
        112.0, 
        120.0  
    ]

    try:
        while True:
            pygame.mixer.music.play()
            start_time = time.time()

            for i in range(len(lines)):
                if not pygame.mixer.music.get_busy():
                    break

                line = lines[i]
                timestamp = timestamps[i]

                # If it's the music intro but the song has already looped past 5 seconds, skip it completely
                pos_ms = pygame.mixer.music.get_pos()
                current_time = (pos_ms / 1000.0) if pos_ms >= 0 else (time.time() - start_time)
                if "music intro" in line and current_time > 5.0:
                    continue

                if i < len(timestamps) - 1:
                    duration = timestamps[i + 1] - timestamp
                else:
                    duration = 3.0  
                duration = max(duration, 0.05)

                while True:
                    pos_ms = pygame.mixer.music.get_pos()
                    current_time = (pos_ms / 1000.0) if pos_ms >= 0 else (time.time() - start_time)
                    if current_time >= timestamp or not pygame.mixer.music.get_busy():
                        break
                    time.sleep(0.001)

                if not pygame.mixer.music.get_busy():
                    break

                if "music intro" in line:
                    console.print(Text(line, style="italic bold deep_sky_blue1"))
                    continue

                char_delay = (duration / max(len(line), 1)) * 0.85
                
                styled = Text()
                for char in line:
                    if not pygame.mixer.music.get_busy():
                        break
                    styled.append(char, style="italic bold deep_sky_blue1")
                    console.print(styled, end="\r")
                    time.sleep(char_delay)
                console.print(styled)  

            while pygame.mixer.music.get_busy():
                time.sleep(0.05)

            if not loop:
                break

    except KeyboardInterrupt:
        console.print("\n[yellow]Stopped by user.[/yellow]")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()


if __name__ == "__main__":
    print_lyrics(loop=True)