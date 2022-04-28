# Continue -- skip the next statement and go back to iteration
# x=[1,3,4,5,5,6,3,3,9]
# for i in x:
#
#      if i==3 :
#          continue
#      print(i)


# break -- to come out of loop
# x=[1,3,4,5,5,6,3,3,9]
# for i in x:
#
#      if i==3 :
#          break
#      print(i)


# Pass  -- to skip the values
# x=[1,3,4,5,5,6,3,3,9]
# for i in x:
#
#      if i==3 :
#          pass
#      print(i)

# building patterns
# for i in range(4):               # first this loop will trigger
#     for j in range(4) :          # then this loop will create 4 # in first row for i
#         print("#",end="")        # it eill just print #
#     print()                      # once it get out of loop it will go to new line and again iteration will start for second time

# new pattern
# for i in range(5):
#     for j in range(5-i):
#         print("#",end="")
#     print()

