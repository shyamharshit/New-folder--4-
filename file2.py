file_read = open('demo.txt', 'r')
print("file in read mode -")
print(file_read.read())
file_read.close()


file_write = open('demo.txt', 'w')
file_write.write("file in write mode ...")
file_write.write("hi! i am a penguin. i am 1yr. old")
file_write.close()

file_append = open('demo.txt', 'a')
file_append.write("\n file in append mode ...")
file_append.write("hi! i am penguin. i am 1yr. old")
file_append.close( )