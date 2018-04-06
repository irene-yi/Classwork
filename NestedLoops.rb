def find_me(arr)
    i = 0
    while i < arr.length
        j = 0
        while j <= arr.length
            if j == arr.length
                return arr[i]
            elsif i == j || -(arr[i]) != arr[j]    
                j += 1
            else
                break
            end
        end
        i += 1
    end
end

arr1 = [1,-1,2,-2,3]

find_me (arr1)


arr0 = [1]
arr1 = [1,-1,2,-2,3]
arr2 = [-3,1,2,3,-1,-4,-2]
arr3 = [1,-1,2,-2,3,3]

arr = arr0