import csv

def ReadWords(file_path):
    unique_words = set()
    with open(file_path, "r") as fileInput:
        reader = csv.reader(fileInput)
        for row in reader:
            if row:  # Kiểm tra nếu dòng không trống
                for cell in row:  # Duyệt qua từng ô trong dòng
                    words = cell.split()  # Tách các từ trong mỗi ô
                    unique_words.update(words)
    return list(unique_words)

def get_existing_words(file_path):
    existing_words = set()
    try:
        with open(file_path, "r") as fileOutput:
            reader = csv.reader(fileOutput)
            for row in reader:
                for word in row:
                    existing_words.add(word.strip())
    except FileNotFoundError:
        pass  # Nếu file không tồn tại, bỏ qua
    return existing_words

def FileOut(file_path, list_word):
    existing_words = get_existing_words(file_path)
    with open(file_path, "a", newline='') as fileOutput:  # Sử dụng mode "a" để append
        writer = csv.writer(fileOutput)
        for word in list_word:
            if word not in existing_words:
                writer.writerow([word])
                existing_words.add(word)  # Cập nhật tập hợp để tránh ghi trùng lặp

def main():
    input_path = "access/First Data/3.csv"
    output_path = "access/Second Data/SecondData.csv"
    list_words = ReadWords(input_path)
    FileOut(output_path, list_words)

if __name__ == "__main__":
    main()
