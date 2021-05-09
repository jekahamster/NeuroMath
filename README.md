# NeuroMath

![Untitled](https://user-images.githubusercontent.com/46385682/117582352-488e3280-b10a-11eb-9a78-3e9d633ef7e2.png)

![ezgif-3-8899addcd0ee](https://user-images.githubusercontent.com/46385682/117583152-4332e700-b10e-11eb-92c4-64406e7fa1aa.gif)

## How to use?

1) First of all, start `install.py` for automatic libs installing. Or you can install it manually (check `lib_versions.txt`). 

![Untitled](https://user-images.githubusercontent.com/46385682/117582845-b176aa00-b10c-11eb-9a54-c0b54a8b87cc.png)

2) After that, you can start `MainApp.py`

![image](https://user-images.githubusercontent.com/46385682/117583611-c35a4c00-b110-11eb-9f9e-8e37fe373e13.png)
![Untitled](https://user-images.githubusercontent.com/46385682/117583782-c6097100-b111-11eb-999d-7ca48795cd14.png)

3) At the next, draw you formula and click __DO IT__ button. 

![Untitled](https://user-images.githubusercontent.com/46385682/117583878-4f20a800-b112-11eb-888d-8e10f2f119d0.png)

4) You can see currect selected symbols (Check information about Finder's below). Click any key on your keyboard

![Untitled](https://user-images.githubusercontent.com/46385682/117583898-65c6ff00-b112-11eb-924d-ffb1b6209c81.png)

5) If formula was not recognized correctly, correct it in the text field and press __Adjust__ to retrain the program (Check information about Adjusting below)


https://user-images.githubusercontent.com/46385682/117583013-8f315c00-b10d-11eb-9df3-df94137eeb60.mp4

## Capabilities

### Settings

`settings.json`
- OperatorsNetworkPath - path to trained network for operators
- NumbersNetworkPath - path to trained network for numbers
- LettersNetworkPath - path to trained network for letters
- CanvasImg - path to your last canvas image 
- NumberLabels - Available numbers
- OperatorLabels - Available operators
- LettersLabels - Available alphabet
- AdjustAll - <br>
0 - retrain only for incorrect symbols. (For exaple: Prog out: `5in(π) = 0.0`, you change to `sin(π) = 0.0` and press __Adjust__, then program retrain only for `s`: `5` -> `s`) <br>
1 - retrain for all symbols (For exaple: Prog out: `5in(π) = 0.0`, you change to `sin(π) = 0.0` and press __Adjust__, then program retrain for all sumbols `5` -> `s`, `i` -> `i`, ...) <br>
Use 1 if model is underfitted (trin model in real time), and 0 for normal models. <br>
- FinderMode - <br>

| Mode               | Overmapping   | Line feed  | Overmapping example  | Line feed example |
| -------------------|---------------|------------|----------------------|-------------------|
| 1                  | YES           | NO         |![Untitled](https://user-images.githubusercontent.com/46385682/117584783-85acf180-b117-11eb-9f50-cacbf55d3506.png)|![Untitled](https://user-images.githubusercontent.com/46385682/117584989-c0635980-b118-11eb-87bb-f0d901e372bc.png)|
| 2 (recomended)     | NO            | YES        |![Untitled](https://user-images.githubusercontent.com/46385682/117584756-58604380-b117-11eb-9648-ecaeeade9c2a.png)|![Untitled](https://user-images.githubusercontent.com/46385682/117585122-58f9d980-b119-11eb-83ef-5a9b9a2f4afc.png)|

- WindowWidth - window width in px
- WindowHeight - window height in px
- WindowResizable - True if resizable else False
- Theme - theme `Dark \ Light` 

![Untitled](https://user-images.githubusercontent.com/46385682/117582550-2b0d9880-b10b-11eb-9c97-d5801fcfd5bc.png)

- PrimaryPalette - Widgets colurs. You can see all possible colors in the PRIMARY_PPALLETES parameter:
Pink, Blue, Indigo, BlueGrey, Brown, LightBlue, Purple, Gray, Yellow, LightGreen, DeepOrange, Green, Red, Teal, Orange, Cyan, Amber, DeepPurple, Lime

![Untitled](https://user-images.githubusercontent.com/46385682/117582433-a589e880-b10a-11eb-9e64-75c657704551.png)


