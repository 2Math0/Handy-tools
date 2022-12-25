import fitz

# deleting pages
class DeletePages:
    def pages_to_list(self,string, seprator):
        if seprator not in string:
            return [int(string)-1]

        #this will make list of numbers
        #int(x) parse each element as int
        #lambda x: int(x) - 1 will make each page number translated into list indexes
        return list(map(lambda x: int(x) - 1, string.split(seprator)))

    def delete_pages(self,path, cutted_pages):
        sys_director = '/' if '/' in path else '\\'
        path_in_sys = path.split(sys_director)[0:-1]
        pdf_name = path.split(sys_director)[-1].split('.')[0]
        #new pdf name
        path_in_sys.append('%s cutted.pdf'%pdf_name)

        f = fitz.open(path)
        f.select(cutted_pages)
        f.save(sys_director.join(path_in_sys))

