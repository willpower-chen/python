# @Author  : Willpower-chen
# @blog: http://www.cnblogs.com/willpower-chen/
from utils.response import BaseResponse
from .base import BaseServiceList
from repository import models
from utils.pager import PageInfo

class IdcService(BaseServiceList):
	def __init__(self):
		condition_config = [
			{'name': 'name', 'text': '机房', 'condition_type': 'input'},
			{'name': 'floor', 'text': '楼层', 'condition_type': 'input'},
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
				'title': "机房",
				'display': 1,
				'text': {'content': "{n}", 'kwargs': {'n': '@name'}},
				'attr': {'edit-enable':'true','edit-type':'input'}  # 自定义属性
			},
			{
				'q': 'floor',
				'title': "楼层",
				'display': 1,
				'text': {'content': "{n}", 'kwargs': {'n': '@floor'}},
				'attr': {'edit-enable':'true','edit-type':'input'}  # 自定义属性
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
		super(IdcService, self).__init__(condition_config, table_config, extra_select)

	def fetch_idc(self, request):
		response = BaseResponse()
		try:
			ret = {}
			conditions = self.assets_condition(request)

			asset_count = models.IDC.objects.filter(conditions).count()
			page_info = PageInfo(request.GET.get('pager', None), asset_count)

			asset_list = models.IDC.objects.filter(conditions).extra(select=self.extra_select).values(
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
