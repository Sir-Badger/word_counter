# RP counter
This python project is a simple algorythm which counts words contained within specified special characters. It's purpose is to provide a robust way to determine the amount of words of roleplay in a message in order to determine experience points for a discord bot. The algorythm provides some customizeability, but it was made with this specific use in mind so it might not be perfect for other uses.

## Usage & installation
In order to use rp counter, you will need run the following command using pip:

```pip install --upgrade rp_counter```

Once installed, using this package is as simple as using it's `count` function. To demonstrate, here's a simple python program utilizing the package:
```py
import rp_counter as rp # import the package

# example message
message="""
    Lorem *This is __valid* text_ ipsum dolor
    > this part of the message is ooc, therefore ignored
    "This is also-" not this "-valid" **This is not valid, as it uses double asterisk instead of single asterisk.**
    """

amount=rp.count(message) # count the words using rp counter

print(f"total words:{amount}") # display the amount of valid rp words
```
___

# The word processing algorithm
In order to determine how many words of roleplay given text contains, we first need to do a few things before counting the individual words. The algorythm goes through the following steps to ensure only words which are contained between special characters (rp indicators) is counted. The default rp indicators are the following characters: `_ * "`, but they can be changed.

- locate all the rp indicators within a message
- sort the indicators into pairs (one at the beggining of roleplay, one at the end)
- filter out the pairs which overlap (`"insert *roleplay* here"` effectively becomes `"insert roleplay here"`)
- go through all the pairs which are left, counting all the words between the rp indicators of that pair

## Locating the characters
This step is fairly simple: given the contents of the message in the form of a string, we go through one character at a time, writing down the position and type if it's one of our designated rp characters. This step also filters out things such as `**this** and __this__`, as those are used within discord's markdown to either embolden or underline text. The basic idea is that roleplay is either surrounded by quotes, or is italic, so flagging bold or underlined text as roleplay would be inaccurate. This step of the algorythm also filters out "out of character" lines within the text. Lines starting with `>` and `-` are ignored by default, though this can be changed.

## Sorting the characters into pairs
Now that we have located the rp indicators, we need to construct pairs out of them which surround the actual words of roleplay. This is done by simply going through the characters, and binding them together sequentially. A rp indicator can only make a pair with an indicator of the same type, meaning that `*lorem ipsum"` does **not** count as a valid rp pair.

## Filtering out overlapping pairs
Given that some pairs might be contained within each other or overlap, we need to remove the redundant ones and join the overlapping ones so that we don't count the words contained in the pairs multiple times. Effectively, two situations can arrise here, the simplified resolution of which is shown below:
 Overlap | Effective result
 --- | ---
 `"Lorem *ipsum" dolor...*` | `"Lorem ipsum dolor...*`
 `"Lorem *ipsum* dolor..."` | `"Lorem ipsum dolor..."`

## Counting the words
What we are left with is the indexes of the beggining and end of each rp pair, giving us substrings of the original message which are surrounded by our specified indicators. Then, ignoring special characters, we split the substrings by spaces (`\n` is replaced with a space character) and return the lenght of the resulting list of valid rp words.