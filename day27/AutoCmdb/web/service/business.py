# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from utils.response import BaseResponse
from .base import BaseServiceList
from repository import models
from utils.pager import PageInfo

class Business(BaseServiceList):
	def __init__(self):
		condition_config = [
			{'name': 'name', 'text': '业务线', 'condition_type': 'input'},
			# {'name': 'name', 'text': '业务联系人', 'condition_type': 'input'},
			{'name': 'manager__name', 'text': '系统管理员', 'condition_type': 'input'},
		]
		table_config = [
			{
				'q': 'id',  # 用于数据库查询的字段，即Model.Tb.objects.filter(*[])
				'title': "ID",  # 前段表格中显示的标题
				'display': 1,  # 是否在前段显示，0表示在前端不显示, 1表示在前端隐藏, 2表示在前段显示
				'text': {'content': "{id}", 'kwargs': {'id': '@id'}},
				'attr': {}  # 自定义属性
			},
			{
				'q': 'name',
				'title': "业务线",
				'display': 1,
				'text': {'content': "{n}", 'kwargs': {'n': '@name'}},
				'attr': {'edit-enable':'true','edit-type':'input'}  # 自定义属性
			},
			# {
			# 	'q': 'contact__name',
			# 	'title': "业务联系人",
			# 	'display': 1,
			# 	'text': {'content': "{n}", 'kwargs': {'n': '@contact__name'}},
			# 	'attr': {'edit-enable': 'true', 'edit-type': 'input'}  # 自定义属性
			# },
			{
				'q': 'manager__name',
				'title': "系统管理员",
				'display': 1,
				'text': {'content': "{n}", 'kwargs': {'n': '@manager__name'}},
				'attr': {'edit-enable': 'true', 'edit-type': 'input'}  # 自定义属性
			},
			{
				'q': 'manager_id',
				'title': "系统管理员ID",
				'display': 0,
				'text': {'content': "{n}", 'kwargs': {'n': '@manager_id'}},
				'attr': {}  # 自定义属性
			},
			{
				'q': None,
				'title': "选项",
				'display': 1,
				'text': {
					'content': "<a href='/xxxxx-{nid}.html'>查看详细</a>",
					'kwargs': {'nid': '@id'}},
				'attr': {}
			},
		]
		extra_select = {}
		super(Business, self).__init__(condition_config, table_config, extra_select)

	def fetch_business(self, request):
		response = BaseResponse()
		try:
			ret = {}
			conditions = self.assets_condition(request)

			asset_count = models.BusinessUnit.objects.filter(conditions).count()
			page_info = PageInfo(request.GET.get('pager', None), asset_count)

			asset_list = models.BusinessUnit.objects.filter(conditions).extra(select=self.extra_select).values(
				*self.values_list)[page_info.start:page_info.end]

			ret['table_config'] = self.table_config
			ret['condition_config'] = self.condition_config
			ret['data_list'] = list(asset_list)
			ret['page_info'] = {
				"page_str": page_info.pager(),
				"page_start": page_info.start,
			}
			ret['global_dict'] = {}
			response.data = ret
			response.message = '获取成功'
		except Exception as e:
			response.status = False
			response.message = str(e)

		return response
