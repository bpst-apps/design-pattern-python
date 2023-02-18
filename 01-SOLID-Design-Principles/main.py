from single_responsibility_principle import Journal, PersistenceManager


# *****************************************************
# SRP Code
journal = Journal()
journal.add_entry('I laughed today.')
journal.add_entry('I ate a meal.')
print(f'Journal Entries:\n{journal}')

print('*'*50)

file = 'journal.txt'
PersistenceManager.save_to_file(journal, file)
with open(file) as fh:
    print(fh.read())

# *****************************************************