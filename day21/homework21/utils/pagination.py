__author__ = 'Administrator'
from django.utils.safestring import mark_safe
class Page:
    '''
    current_page当前页
    data_count总数据
    per_page_count每页显示数据个数
    pager_num每页显示页码数
    @property 装饰一个方法变成属性来调用
    '''
    def __init__(self,current_page,data_count,per_page_count=10,pager_num=7):
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.pager_num = pager_num
    #当前页显示的起始页
    @property
    def start(self):
        return (self.current_page-1) * self.per_page_count
    #当前页面显示的末页
    @property
    def end(self):
        return self.current_page * self.per_page_count
    #总页数
    @property
    def total_count(self):
        #divmod取商和余数v为商，y为余数
        v,y = divmod(self.data_count, self.per_page_count)
        #当余数不为0时，总页数加一
        if y:
            v += 1
        return v
    #base_url就是url路由
    def page_str(self, base_url):
        page_list = []
        #当总页数小于，每页显示的页数时
        if self.total_count < self.pager_num:
            start_index = 1
            end_index = self.total_count + 1
        #当总页数大于，每页显示的页数时
        else:
            if self.current_page <= (self.pager_num+1)/2:
                start_index = 1
                end_index = self.pager_num + 1
            else:
                start_index = self.current_page - (self.pager_num-1)/2
                end_index = self.current_page + (self.pager_num+1)/2
                if (self.current_page + (self.pager_num-1)/2) > self.total_count:
                    end_index = self.total_count + 1
                    start_index = self.total_count - self.pager_num + 1
        #上一页，如果当前页数为1时，点击上一页href="javascript:void(0);"代表不做任何操作
        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0);">上一页</a>'
        else:
            prev = '<a class="page" href="%s?p=%s">上一页</a>' %(base_url,self.current_page-1,)
        page_list.append(prev)

        for i in range(int(start_index),int(end_index)):
            if i ==self.current_page:
                temp = '<a class="page active" href="%s?p=%s">%s</a>' %(base_url,i,i)
            else:
                temp = '<a class="page" href="%s?p=%s">%s</a>' %(base_url,i,i)
            page_list.append(temp)
        #下一页，如果下一页等于总页数时，点击下一页href="javascript:void(0);"代表不做任何操作
        if self.current_page == self.total_count:
            nex = '<a class="page" href="javascript:void(0);">下一页</a>'
        else:
            nex = '<a class="page" href="%s?p=%s">下一页</a>' %(base_url,self.current_page+1,)
        page_list.append(nex)

        #跳转 val是获取当前输入的页码值，然后location.href跳转到后面的base+val字符串拼接
        # jump = """
        # <input type='text'  /><a onclick='jumpTo(this, "%s?p=");'>GO</a>
        # <script>
        #     function jumpTo(ths,base){
        #         var val = ths.previousSibling.value;
        #         location.href = base + val;
        #     }
        # </script>
        # """ %(base_url,)
        jump = """
        <input type='text'  /><input type='button' value='GO' onclick='jumpTo(this, "%s?p=");' />
        <script>
            function jumpTo(ths,base){
                var val = ths.previousSibling.value;
                location.href = base + val;
            }
        </script>
        """ %(base_url,)

        page_list.append(jump)

        #以下加mark_safe，是为了确保后台定义字符串包含特殊的html字符，前端可以做解析
        page_str = mark_safe("".join(page_list))

        return page_str