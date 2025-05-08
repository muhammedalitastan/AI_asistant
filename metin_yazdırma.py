import keyboard
import time


fast = 0.03
zaman = 5

text = """The second presentation was highly successful due to a wide range of strengths in both delivery and content organization, demonstrating what an effective presentation should look like. First and foremost, the speaker appeared extremely well-prepared and confident. This confidence was reflected in the speaker's body language, which was open, relaxed, and engaging. The presenter maintained strong and consistent eye contact with the audience, creating a direct and personal connection that made listeners feel involved and respected. The delivery of the speech itself was lively and dynamic. The speaker used a variety of vocal techniques, such as changing pitch, pace, and volume, to emphasize important points and keep the audience emotionally engaged. Moments of excitement were highlighted by raising the voice slightly, while serious points were delivered with a slower, more thoughtful tone. This variation kept the presentation interesting and helped underline key ideas clearly. The speaker also used purposeful gestures and movement around the stage to reinforce main points and to create a sense of energy and enthusiasm throughout the presentation.One of the major improvements over the first presentation was the use of well-designed visual aids. The slides were clean, minimalistic, and directly relevant to the spoken content. Key ideas were summarized using short bullet points, and supportive visuals like images, charts, and diagrams helped the audience to better understand and remember the information. Instead of overwhelming the audience with text, the visuals complemented the speaker’s words and made the presentation more visually appealing.In terms of structure, the second presentation was clearly and logically organized. It began with a strong introduction that not only presented the topic but also captured the audience’s attention with an interesting fact or question. The body of the speech was divided into clear sections, each focusing on a main idea and supported with examples or evidence. Transitions between points were smooth and signaled clearly, helping the audience follow the flow of the argument easily. Finally, the conclusion effectively summarized the main points and left the audience with a memorable final thought or call to action.Another key factor was the speaker’s success in engaging the audience. Throughout the presentation, the speaker asked rhetorical and direct questions, shared personal stories, and used humor appropriately to create a friendly and interactive atmosphere. This approach not only maintained the audience’s interest but also made the content feel more relatable and meaningful. Furthermore, the speaker showed genuine passion and enthusiasm for the topic, which was infectious and helped to motivate and inspire the audience.
"""

# Geri sayım başlat
for i in range(zaman, 0, -1):
    print(f"Metin yazılmadan önce bekleniyor... {i} saniye kaldı", end="\r")
    time.sleep(1)

print("\nBaşlıyor...")

# Metni harf harf yazdır (Türkçe karakter desteği ile)
for char in text:
    keyboard.write(char)
    time.sleep(fast)

print("Metin başarıyla yazıldı!")