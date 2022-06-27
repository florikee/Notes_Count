#Calculate_Rupees_In_Notes

def calculate_rupees_in_notes(rupees):
    if rupees > 1000000:
        print('Numri duhet të jetë më i vogël se 1000000')
    notes = [1000, 500, 100, 50, 20, 10, 5, 2, 1]   #1
    notes_count = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 1
    memo = { } # 1

    for i in range(len(notes)):    # n
        notes_count[i] = rupees // notes[i] # 1
        rupees = rupees % notes[i]  # 1
        if notes[i] in memo:
            notes_count[i] += memo[notes[i]]
        else:
            memo[notes[i]] = notes_count[i]

        #komplet ekseutohet 1her + 1 here brenda if ose else
    
    return memo #1


#big O notation:
# O (n + 8) = O (n)


if __name__ == '__main__':
    rupees = int(input("Enter the amount in rupees: "))
    notes_count = calculate_rupees_in_notes(rupees)
    print("Notes count: ", notes_count)
