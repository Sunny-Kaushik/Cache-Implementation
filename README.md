# Cache-Implementation
This project is a an application of memory based cache implementation on least recently used policy created in python, presenting the miss and hit rates by varying block size and by changing the associativity.
Keywords:
1) Block Size: Caches are divided into blocks, which may be of various sizes, the number of blocks is usually in the power of 2, here in our project we have created caches with varying block sizes like 1, 2, 4, 8, 16.
2) Associativity: In a set-associative cache, there are a fixed number of locations (called a set) in which a given address may be stored. The number of locations in each set is associated with the cache.
3) Index: The index cache is a portion of the machine's memory allocated to caching the data of specific terms sent to the Content component during index actions. Using the index cache speeds up indexing because writing to memory is quicker than writing to disk.
4) Tag: Every line stores a tag, which is certain upper bits of the physical address. Hence, by looking at the tag (after having zeroed in on which cache line to look at), we can decide whether the request was a hit or a miss.

How to run the code:
Visual Studio :
—> Open the file “$file_name$.py”
in visual studio and simply right-click and choose to run option or go to the rightmost top corner and click the arrow icon.

a) We need 2 to the power 15 (2**15) lines.

—>We are implementing cache which is a special storage space for temporary files that makes a device, browser, or app run faster and more efficiently.
—>We create a two-dimensional array one maintaining the number of lines and the other maintaining number of ways. We can find the number of the lines using the formula(size of cache/block size * the number of ways).Log base 2 of (number of lines ) is the number of the index bits, As the cache is four-way we can say that the number of bits for byte offset is 2 and as the number of bits is 32 number of bits for the tag is (32-(index bits +byte offset)).
—>We take input from the file and separate the required address from each line using slicing.
—>We get the required tag bits, and index bits from the sliced address and now we match the index to the line number and insert the tag into the ways in order of LRU(least recently used) which removes the element which was least recently used when it comes to the situation of overwriting away.
—>Increase the count value if there is a hit (tag match and index match ) for some other input value.
—>And we finally print the hit rate and the miss rate.

b)
—>We are implementing cache which is a special storage space for temporary files that makes a device, browser, or app run faster and more efficiently.
—>We create a two-dimensional array one maintaining the number of lines and the other maintaining number of ways. We can find the number of the lines using the formula(size of cache/block size * the number of ways).Log base 2 of (number of lines ) is the number of the index bits, As the cache is four-way we can say that the number of bits for byte offset is 2 and as the number of bits is 32 number of bits for the tag is (32-(index bits +byte offset)).
—>We take input from the file and separate the required address from each line using slicing.
—>We get the required tag bits, and index bits from the sliced address and now we match the index to the line number and insert the tag into the ways in order of LRU(least recently used) which removes the element which was least recently used when it comes to the situation of overwriting away.
—>Increase the count value if there is a hit (tag match and index match ) for some other input value.
—>And we finally print the hit rate and the miss rate.

c)
—>In this part keeping the cache size 512 kB we are varying block size from 1 byte, 4 bytes, 8 bytes, and 16 bytes.
—>Increasing the block size means we are storing more amount of data in individual blocks.
—>Although this increases the hit rate but there are some disadvantages.
The larger the block size, the less the number of entries in the cache, and the more the competition between program data for these entries!
The larger the block size, the more time it takes to fetch this block size from memory.

d)
—> In this part we are varying the associativity from 1, 2, 4, 8, and 16 wherein according to the associativity, we will change tag and index.
—> Associativity is the size of these sets, or, in other words, how many different cache lines each data block can be mapped to. Higher associativity allows for more efficient utilisation of cache but also increases the cost.
Graphs show the increase in hit rates as we increase the associa/vity from 1,2, 4, 8, and 16 in different test cases.(find it with the attached codes)

