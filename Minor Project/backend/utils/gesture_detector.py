# import cv2
# import mediapipe as mp

# # Function to detect gestures (simplified for demonstration)
# def detect_gesture():
#     mp_hands = mp.solutions.hands
#     hands = mp_hands.Hands()
#     cap = cv2.VideoCapture(0)

#     while True:
#         success, image = cap.read()
#         image = cv2.flip(image, 1)
#         results = hands.process(image)

#         if results.multi_hand_landmarks:
#             # Add gesture detection logic here (e.g., swipe left/right)
#             # Return detected gesture as a string
#             return "next"  # Example: Return "next" if right swipe detected

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     cap.release()
#     cv2.destroyAllWindows()
