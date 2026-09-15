from fastapi import APIRouter

router = APIRouter(prefix="/atbash", tags=["atbash"])



@router.get("/{word}")
def health_check(word):
    word = word.lower()
    newWord = []
    hebrew_alphabet = [
    'א', 'ב', 'ג', 'ד', 'ה', 'ו', 'ז', 'ח', 'ט', 'י', 'כ',
    'ל', 'מ', 'נ', 'ס', 'ע', 'פ', 'צ', 'ק', 'ר', 'ש', 'ת']
    english_alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if word[0] in hebrew_alphabet:
        for letter in word:
            for i , let in enumerate(hebrew_alphabet):
                if letter == let:
                    newWord.append(hebrew_alphabet[i])
                    break
    if word[0] in english_alphabet:
            for letter in word:
                for i , let in enumerate(english_alphabet):
                    if letter == let:
                        newWord.append(english_alphabet[i])
                        break
        

    return {"status" :200 , "result": newWord}




