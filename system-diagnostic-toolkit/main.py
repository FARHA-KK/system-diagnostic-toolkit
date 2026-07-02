from system_info import get_system_info
from cpu_info import get_cpu_info
from memory_info import get_memory_info
from disk_info import get_disk_info
from network_info import get_network_info


def display_info(title, info):
    print("\n" + "=" * 50)
    print(title.center(50))
    print("=" * 50)

    for key, value in info.items():
        print(f"{key:<25}: {value}")

    print("=" * 50)


def show_menu():
    print("\n")
    print("=" * 50)
    print(" SYSTEM DIAGNOSTIC TOOLKIT ".center(50, "="))
    print("=" * 50)
    print("1. System Information")
    print("2. CPU Information")
    print("3. Memory Information")
    print("4. Disk Information")
    print("5. Network Information")
    print("6. View Complete Report")
    print("7. Exit")
    print("=" * 50)


def main():
    while True:
        show_menu()

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            display_info("SYSTEM INFORMATION", get_system_info())

        elif choice == "2":
            display_info("CPU INFORMATION", get_cpu_info())

        elif choice == "3":
            display_info("MEMORY INFORMATION", get_memory_info())

        elif choice == "4":
            display_info("DISK INFORMATION", get_disk_info())

        elif choice == "5":
            display_info("NETWORK INFORMATION", get_network_info())

        elif choice == "6":
            display_info("SYSTEM INFORMATION", get_system_info())
            display_info("CPU INFORMATION", get_cpu_info())
            display_info("MEMORY INFORMATION", get_memory_info())
            display_info("DISK INFORMATION", get_disk_info())
            display_info("NETWORK INFORMATION", get_network_info())

        elif choice == "7":
            print("\nThank you for using System Diagnostic Toolkit.")
            break

        else:
            print("\nInvalid choice! Please enter a number between 1 and 7.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()