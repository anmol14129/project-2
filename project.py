

            else:
                num_of_tries-=1
                print("PIN incorrect! Number of tries left -", num_of_tries, end = "\n\n")

        else:
            print("Exiting...")
            
            t.sleep(2)
            print("You have been logged out. Thank you!\n\n")
            break


    else:
        print("Invalid input!")
        print("\t\t0. Enter 0 to Logout and Exit!")
        continue