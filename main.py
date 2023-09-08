
def count_batteries_by_health(present_capacities):
  SOH=100*(present_capacities/120) //calculate soh
  if(SOH>=80 and SOH<=100):
    healthy+=1 //check healthy condition if yes increase its count
  elif(SOH<80 and SOH>=65):
    exchange+=1 //check excahnge condition if yes increase its count
  else:
    failed+=1  //else increase failed count
  return {
    "healthy": healthy,
    "exchange": exchange,
    "failed": failed
  }


def test_bucketing_by_health():
  print("Counting batteries by SoH...\n")
  present_capacities = [115, 118, 80, 95, 91, 77]
  counts = count_batteries_by_health(present_capacities)
  assert(counts["healthy"] == 2)
  assert(counts["exchange"] == 3)
  assert(counts["failed"] == 1)
  print("Done counting :)")


if __name__ == '__main__':
  test_bucketing_by_health()
