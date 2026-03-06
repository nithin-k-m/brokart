from django import template

register = template.Library()# to register the custom template tag in the application, so that we can use this custom template tag in our templates

@register.filter(name='chunks')# to register the custom template filter in the application, so that we can use this custom template filter in our templates with the name 'raw_chunks'
def row_chunks(list_data, chunk_size):# custom template filter function to split the list of products into chunks of specified size, so that we can display the products in rows in the product listing page of the application
    chunk=[]# to store the chunks of products
    i=0# to keep track of the number of products in the current chunk
    for data in list_data:# iterating through the list of products
        chunk.append(data)# appending the product to the chunk list
        i+=1# incrementing the counter variable by 1
        if i==chunk_size:# if the counter variable is equal to the chunk size then we have reached the end of the current chunk
            yield chunk# yielding the current chunk of products to the template, so that we can display the products in rows in the product listing page of the application
            i=0# resetting the counter variable to 0 for the next chunk of products
            chunk=[]# resetting the chunk list to store the next chunk of products
    if chunk:# if there are some remaining products in the last chunk then we need to yield that chunk to the template, so that we can display the products in rows in the product listing page of the application, this is for the case when the total number of products is not a multiple of the chunk size and we have some remaining products in the last chunk 
         yield chunk# yielding the last chunk of products to the template, so that we can display the products in rows in the product listing page of the application, this is for the case when the total number of products is not a multiple of the chunk size and we have some remaining products in the last chunk        
        



