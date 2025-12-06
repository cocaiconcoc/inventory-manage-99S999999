songs = []
def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ").strip()
        if choice == '1':
            prompt_add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            prompt_search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập 1-4.")

if __name__ == "__main__":
    main()