student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

lowest_score = student_scores[0]
for score in student_scores:
  if score < lowest_score:
    lowest_score = score


print(lowest_score)
  