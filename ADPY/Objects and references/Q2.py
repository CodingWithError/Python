class ExamSubmission:
  def __init__(self,examinee: str,points: str):
    self.student=examinee
    self.points=points

def passed(submissions: list, lowest_passing: int):
  passed_list=[]
  for i in submissions:
    if i.points>=lowest_passing:
      passed_list.append(f'ExamSubmission (examinee: {i.student}, points: {i.points})')

  return passed_list


if __name__ == "__main__":
    s1 = ExamSubmission("Peter", 12)
    s2 = ExamSubmission("Pippa", 19)
    s3 = ExamSubmission("Paul", 15)
    s4 = ExamSubmission("Phoebe", 9)
    s5 = ExamSubmission("Persephone", 17)

    passes = passed([s1, s2, s3, s4, s5], 15)
    for passing in passes:
        print(passing)