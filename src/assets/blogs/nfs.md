# Teaching AI to Dominate the Streets: Self-Driving in Need for Speed: Most Wanted

Hey there, speed demons and AI enthusiasts! It's your boy Mike, back with another crazy deep learning project. Today, we're gonna marry two of my favorite things: artificial intelligence and illegal street racing. That's right, we're teaching an AI to drive in Need for Speed: Most Wanted (2005)!

Before we dive in, huge shoutout to the folks who've already done some groundwork on this. I've been referencing this awesome GitHub repo: [Need-For-Speed-Self-driving](https://github.com/strcoder4007/Need-For-Speed-Self-driving). If you're interested in this kind of stuff, definitely check it out!

Now, buckle up and let's hit the nitrous on this project!

## The Grand Idea

So here's the deal: we're going to create an AI that can drive a car in Need for Speed: Most Wanted. We'll use a convolutional neural network (CNN) to process images from the game and output steering commands. It's like teaching a teenager to drive, except our AI can't blame its mistakes on hormones.

## Data Gathering: Playing the Game (Badly)

First things first, we need data. And in the world of supervised learning, that means we gotta play the game ourselves. A lot. Here's how I set up the data collection:

```python
import numpy as np
import cv2
import time
from grabscreen import grab_screen
from getkeys import key_check
import os

def keys_to_output(keys):
    #[A,W,D]
    output = [0,0,0]
    
    if 'A' in keys:
        output[0] = 1
    elif 'D' in keys:
        output[2] = 1
    else:
        output[1] = 1
    return output

file_name = 'training_data.npy'

if os.path.isfile(file_name):
    print('File exists, loading previous data!')
    training_data = list(np.load(file_name, allow_pickle=True))
else:
    print('File does not exist, starting fresh!')
    training_data = []

def main():
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        if not paused:
            screen = grab_screen(region=(0,40,800,640))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120))
            keys = key_check()
            output = keys_to_output(keys)
            training_data.append([screen,output])
            
            if len(training_data) % 1000 == 0:
                print(len(training_data))
                np.save(file_name,training_data)

        keys = key_check()
        if 'T' in keys:
            if paused:
                paused = False
                print('unpaused!')
                time.sleep(1)
            else:
                print('Pausing!')
                paused = True
                time.sleep(1)

main()
```

This script captures the game screen, resizes it, converts it to grayscale, and saves it along with the key presses. I ran this while playing the game for hours. And let me tell you, trying to drive well while also making sure your data collection script isn't crashing is... an experience.

## Preparing the Data: From Pixels to Tensors

Once we've got our data, we need to prepare it for our model. Here's how I processed the data:

```python
import numpy as np
from sklearn.model_selection import train_test_split
import cv2

data = np.load('training_data.npy', allow_pickle=True)

X = np.array([i[0] for i in data])
y = np.array([i[1] for i in data])

X = X.reshape(-1, 120, 160, 1)
X = X / 255.0  # Normalize pixel values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")
```

## The Brain of our Driver: InceptionResNetV2

For our model, we're going with the InceptionResNetV2 architecture. It's like giving our AI driver a supercomputer for a brain. Here's how we set it up:

```python
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

base_model = InceptionResNetV2(weights='imagenet', include_top=False, input_shape=(120, 160, 3))

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
predictions = Dense(3, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = False

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

## Training the Beast: Let the Games Begin!

Now it's time to train our model. This is where the magic happens... and where your GPU starts to sweat.

```python
history = model.fit(
    X_train, y_train,
    validation_data=(X_test, y_test),
    epochs=10,
    batch_size=32
)

model.save('nfs_driver_model.h5')
```

I ran this for about 10 epochs. It took forever, and I'm pretty sure my GPU was plotting revenge against me by the end.

## The Moment of Truth: Testing Our AI Driver

After the training, it was time to see if our AI could actually drive without crashing every two seconds. Here's the script I used to test it:

```python
import numpy as np
from grabscreen import grab_screen
import cv2
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
from tensorflow.keras.models import load_model

model = load_model('nfs_driver_model.h5')

def straight():
    PressKey(W)
    ReleaseKey(A)
    ReleaseKey(D)

def left():
    PressKey(A)
    ReleaseKey(W)
    ReleaseKey(D)
    ReleaseKey(A)

def right():
    PressKey(D)
    ReleaseKey(A)
    ReleaseKey(W)
    ReleaseKey(D)

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False
    while(True):
        if not paused:
            screen = grab_screen(region=(0,40,800,640))
            print('loop took {} seconds'.format(time.time()-last_time))
            last_time = time.time()
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
            screen = cv2.resize(screen, (160,120))

            prediction = model.predict([screen.reshape(-1,120,160,1)])[0]
            moves = list(np.around(prediction))
            print(moves, prediction)

            if moves == [1,0,0]:
                left()
            elif moves == [0,1,0]:
                straight()
            elif moves == [0,0,1]:
                right()

        keys = key_check()

        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                ReleaseKey(A)
                ReleaseKey(W)
                ReleaseKey(D)
                time.sleep(1)

main()
```

## The Good, The Bad, and The "How Did It End Up There?!"

Now, I'd love to tell you that my AI immediately started driving like Vin Diesel in The Fast and the Furious. But let's be real, this is machine learning we're talking about. Here are some of the speed bumps I hit along the way:

1. **Data Imbalance**: Turns out, I'm a boring driver. Most of my training data was just driving straight. The AI learned this really well and would often just plow straight into walls. I had to intentionally oversample turns to balance things out.

2. **Overfitting**: At one point, my AI got really good at driving on one particular track... and absolutely terrible everywhere else. It was like it had memorized that one route and forgot how to actually drive.

3. **The "Indecisive Driver" Syndrome**: Sometimes, the AI would rapidly switch between turning left and right, making the car wiggle down the road like it had one too many virtual beers. Implementing a small delay between actions helped smooth this out.

4. **Performance Issues**: Running the game, screen capture, and neural network inference all at once was... challenging. My poor laptop sounded like it was trying to achieve liftoff. I had to optimize my code and lower the game's graphics settings to get everything running smoothly.

5. **The "Ghost Driver" Bug**: There was a period where my AI would sometimes just... stop. The car would coast to a halt and sit there, completely unresponsive. Turned out to be a sneaky bug in my key press simulation code.

6. **Unexpected Obstacles**: The AI did great on empty roads, but throw in some traffic or cops, and it was mayhem. Teaching it to handle dynamic obstacles is a whole other challenge I'm still working on.

## What's Next? More Power!

So, where do we go from here? Well, there's still a lot to improve:

1. **More Data**: Always more data. I'm thinking of setting up a rig to automatically gather training data while I sleep. Who needs rest when you can have your computer play video games for you?

2. **Dynamic Obstacle Handling**: Teaching the AI to deal with other cars, cops, and maybe even those pesky pedestrians who always seem to jump in front of you at the worst times.

3. **Speed Control**: Right now, our AI is basically a lead-foot driver always flooring it. Teaching it when to slow down could be interesting.

4. **Multi-Task Learning**: Maybe we could teach it not just to drive, but to complete races or evade cops. Now that would be cool!

## Wrapping Up

And there you have it, folks! We've taken our first steps into teaching an AI to be a street racer. It's been a wild ride, full of crashes (both in-game and code), late nights, and more energy drinks than I care to admit.

Remember, the code in this blog is just a starting point. There's a ton of room for optimization and improvement. Feel free to take this idea and run with it! And if you make any cool improvements, let me know. I'm always down to see some AI street racing action.

Until next time, keep your code clean and your nitrous tanks full!

Catch you on the streets,
Mike

P.S. Shoutout again to the [Need-For-Speed-Self-driving](https://github.com/strcoder4007/Need-For-Speed-Self-driving) repo. Those folks are doing some seriously cool stuff!
