def getMinCost(crew_id, job_id):
    crew_id.sort()
    job_id.sort()
    total_walk = 0
    for i in range(len(crew_id)):
        walk = abs(crew_id[i] - job_id[i])
        total_walk = total_walk + walk

    return total_walk


crew = [1, 3, 5]
job = [3, 5, 7]
print(getMinCost(crew, job))
