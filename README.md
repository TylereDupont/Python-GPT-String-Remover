# GPT String Remover

Quickly (One Click) remove GPT text strings such as markdown formatting using the gui of this python script. 

One click paste, process and copy input.
## Requirements

- pyperclip

```
pip install pyperclip
```

OR

```
pip install -r requirements.txt
```

### Using venv

```
cd path\to\script
```

```
pythom -m venv venv
```

**For Windows**
```
.\venv\Scripts\activate
```

**For Linux/mac**
```
source venv/bin/activate
```

```
pip install pyperclip
```

OR

```
pip install -r requirements.txt
```

## Usage

```
python remove.py
```

![[3.png]]

- Press copy button on GPT output
  
  ![[1.png]]
  
  It looks like this, I want to remove the bolding markdown:
  
  ![[2.png]]
  
- Enter strings to remove in top text box of remove.py gui
- press Paste, Process, and Copy button
  
  ![[4.png]]

Processed text is copied to your clipboard automatically and it is stored in the lower text box until a new input is processed

![[5.png]]
Output:

![[6.png]]

Removing last piece of text as well:

![[7.png]]
