#!/usr/bin/python3
def calc_weight(list_=[]):
  if len(list_) == 0:
      return 0
  else:
      calc_s = sum(map(lambda score: score[0] * score[1], list_))
      calc_w = sum(map(lambda weight: weight[1], list_))
  return calc_s/calc_w
        

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
