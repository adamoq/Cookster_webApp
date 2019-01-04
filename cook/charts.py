from chartjs.views.lines import BaseLineChartView
from .models import Category, Product, WaiterOrder, WaiterTask, CookTask, CookOrder
#MENU
class DishChartJSONView(BaseLineChartView):
	def get_providers(self):
		namesList = []
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			namesList.append(dish)
		return list(set(namesList))

	def get_labels(self):
		return [['',],]

	def get_data(self):
		"""Return 3 datasets to plot."""
		
		namesList = []
		dishesList = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			dish = task.dish.id
			if dish in map : map[dish] =+ task.count
			else : map[dish] = task.count
			namesList.append(dish)
		for task in list(set(namesList)):
			dishesList.append([map[task],])
		return dishesList	

class CategoryChartJSONView1(BaseLineChartView):

	def get_labels(self):
		namesList = []
		for task in WaiterOrder.objects.all():
			dish = task.dish.name
			namesList.append(dish)
		return list(set(namesList))


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		tasklist = []
		namesList = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			dish = task.dish.id
			if dish in map : map[dish] =+ task.count
			else : map[dish] = task.count
			namesList.append(dish)
		for task in list(set(namesList)):
			tasklist.append(map[task])
		return [tasklist]	

class CategoryChartJSONView(BaseLineChartView):

	def get_labels(self):
		list = []
		for prod in Category.objects.all():
			list.append(prod.category_name)
		return list


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list2 = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			cat = task.dish.category.id
			if cat in map : map[cat] =+ task.count
			else : map[cat] = task.count
		
		for category in Category.objects.all():
			try:
				list2.append(map[category.id])
			except KeyError:
				list2.append(0)
		return [list2]		

class CategoryChartJSONView2(BaseLineChartView):

	def get_labels(self):
		list = []
		for prod in Category.objects.all():
			list.append(prod.category_name)
		return list


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		list2 = []
		x = 2
		map = {}
		for task in WaiterOrder.objects.all():
			cat = task.dish.category.category_name
			if cat in map : map[cat] =+ task.price_default
			else : map[cat] = task.price_default
		
		for category in Category.objects.all():
			try:
				el = map[category.category_name]
				list2.append(el)
			except KeyError:
				list2.append(0)
		return [list2]

dish_chart_json = DishChartJSONView.as_view()		
category_chart_json = CategoryChartJSONView.as_view()
category_chart_json1 = CategoryChartJSONView1.as_view()
category_chart_json2 = CategoryChartJSONView2.as_view()

#ZAMÓWIENIA KUCHARZY
class CookOrderChartJSONView(BaseLineChartView):

	def get_providers(self):
		import datetime
		namesList = []

		for dayas in range (28, -1, -1):
			#namesList.append("dish"+str(dayas))
			today_min = datetime.date.today() - datetime.timedelta(days = dayas)
			namesList.append(str(today_min.strftime("%d"))+'.'+str(today_min.strftime("%m")))
			
		return namesList
		#dishesList.append([queryste,])

	def get_labels(self):
		return [['',],]

	def get_data(self):
		import datetime
		"""Return 3 datasets to plot."""
		dishesList = []
		today_min = datetime.date.today().strftime("%Y")
		today_minm = datetime.date.today().strftime("%m")
		today_mind = datetime.date.today().strftime("%d")
		today_min = datetime.date.today() + datetime.timedelta(days = 2)
		today_minm = datetime.datetime.now() - datetime.timedelta(days = 1)
		today_mind = datetime.date.today().strftime("%d")

			
		#return dishesList
		#queryset = CookTask.objects.filter(created_at__year = today_min, created_at__month = today_minm, created_at__day = today_mind)



		for dayaaas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayaaas)			
			queryste = CookTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d"))
			dishesList.append([len(queryste),])
		return dishesList	

class CookOrderChart2JSONView(BaseLineChartView):
	def get_labels(self):
		namesList = []
		for task in CookTask.objects.all():
			dish = task.cook.name + " " + task.cook.surname
			namesList.append(dish)
		return list(set(namesList))


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		
		namesList = []
		dishesList = []
		x = 2
		dishmap = {}
		for task in CookTask.objects.all():
			dish = task.cook.name + " " + task.cook.surname
			if dish in dishmap : dishmap[dish] += 1
			else : dishmap[dish] = 1
			namesList.append(dish)
		for task in list(set(namesList)):
			dishesList.append([dishmap[task],])
		return [dishesList]

class CookOrderChart3JSONView(BaseLineChartView):
	def get_labels(self):
		namesList = []
		for task in CookTask.objects.all():
			dish = task.provider.name + " " + task.provider.surname
			namesList.append(dish)
		return list(set(namesList))


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		
		namesList = []
		dishesList = []
		x = 2
		dishmap = {}
		for task in CookTask.objects.all():
			dish = task.provider.name + " " + task.provider.surname
			if dish in dishmap : dishmap[dish] += 1
			else : dishmap[dish] = 1
			namesList.append(dish)
		for task in list(set(namesList)):
			dishesList.append([dishmap[task],])
		return [dishesList]
class CookOrderChart4JSONView(BaseLineChartView):

	def get_labels(self):
		import datetime
		namesList = []

		for dayas in range (28, -1, -1):			
			today_min = datetime.date.today() - datetime.timedelta(days = dayas)		
			taskscount = CookTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			if taskscount > 0 : 
				namesList.append(str(today_min.strftime("%d"))+'.'+str(today_min.strftime("%m")))
		return namesList

	def get_data(self):
		import datetime
		"""Return 3 datasets to plot."""
		dishesList = []

		for dayaaas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayaaas)			
			taskscount = CookTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			if taskscount > 0 : dishesList.append([taskscount,])
		return [dishesList]

cookorders_chart_json = CookOrderChartJSONView.as_view()		
cookorders_chart_json2 = CookOrderChart2JSONView.as_view()
cookorders_chart_json3 = CookOrderChart3JSONView.as_view()
cookorders_chart_json4 = CookOrderChart4JSONView.as_view()

#ZAMÓWIENIA KELNERÓW
class WaiterOrderChartJSONView(BaseLineChartView):

	def get_providers(self):
		import datetime
		namesList = []

		for dayas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayas)
			namesList.append(str(today_min.strftime("%d"))+'.'+str(today_min.strftime("%m")))
			
		return namesList

	def get_labels(self):
		return [['',],]

	def get_data(self):
		import datetime
		"""Return 3 datasets to plot."""
		dishesList = []

		for dayaaas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayaaas)			
			queryste = WaiterTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			dishesList.append([queryste,])
		return dishesList	

class WaiterOrderChart2JSONView(BaseLineChartView):
	def get_labels(self):
		namesList = []
		for task in WaiterTask.objects.all():
			dish = task.waiter.name + " " + task.waiter.surname
			namesList.append(dish)
		return list(set(namesList))


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		
		namesList = []
		dishesList = []
		x = 2
		dishmap = {}
		for task in WaiterTask.objects.all():
			dish = task.waiter.name + " " + task.waiter.surname
			if dish in dishmap : dishmap[dish] += 1
			else : dishmap[dish] = 1
			namesList.append(dish)
		for task in list(set(namesList)):
			dishesList.append([dishmap[task],])
		return [dishesList]

class WaiterOrderChart3JSONView(BaseLineChartView):
	def get_labels(self):
		namesList = []
		for task in WaiterTask.objects.all():
			dish = task.cook.name + " " + task.cook.surname
			namesList.append(dish)
		return list(set(namesList))


	def get_data(self):
		"""Return 3 datasets to plot."""
		
		
		namesList = []
		dishesList = []
		x = 2
		dishmap = {}
		for task in WaiterTask.objects.all():
			dish = task.cook.name + " " + task.cook.surname
			if dish in dishmap : dishmap[dish] += 1
			else : dishmap[dish] = 1
			namesList.append(dish)
		for task in list(set(namesList)):
			dishesList.append([dishmap[task],])
		return [dishesList]
class WaiterOrderChart4JSONView(BaseLineChartView):

	def get_labels(self):
		import datetime
		namesList = []

		for dayas in range (78, -1, -1):			
			today_min = datetime.date.today() - datetime.timedelta(days = dayas)		
			taskscount = WaiterTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			if taskscount > 0 : 
				namesList.append(str(today_min.strftime("%d"))+'.'+str(today_min.strftime("%m")))
		return namesList

	def get_data(self):
		import datetime
		"""Return 3 datasets to plot."""
		dishesList = []

		for dayaaas in range (78, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayaaas)			
			taskscount = WaiterTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			if taskscount > 0 : dishesList.append([taskscount,])
		return [dishesList]

waiterorders_chart_json = WaiterOrderChartJSONView.as_view()		
waiterorders_chart_json2 = WaiterOrderChart2JSONView.as_view()
waiterorders_chart_json3 = WaiterOrderChart3JSONView.as_view()
waiterorders_chart_json4 = WaiterOrderChart4JSONView.as_view()

#PRODUKTY
class ProductChartJSONView(BaseLineChartView):


	def get_providers(self):
		import datetime
		namesList = []

		for dayas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayas)
			namesList.append(str(today_min.strftime("%d"))+'.'+str(today_min.strftime("%m")))
			
		return namesList

	def get_labels(self):
		return [['',],]

	def get_data(self):
		import datetime
		"""Return 3 datasets to plot."""
		dishesList = []

		for dayaaas in range (28, -1, -1):
			today_min = datetime.date.today() - datetime.timedelta(days = dayaaas)			
			queryste = WaiterTask.objects.filter(created_at__year = today_min.strftime("%Y"), created_at__month = today_min.strftime("%m"), created_at__day = today_min.strftime("%d")).count()
			dishesList.append([100+dayaaas,])
		return dishesList	
from random import shuffle, randint
class ProductChart2JSONView(BaseLineChartView):


    def get_providers(self):
        """Return names of datasets."""
        return ["Central", "Eastside", "Westside"]

    def get_labels(self):
        """Return 7 labels."""
        return ["January", "February", "March", "April", "May", "June", "July"]

    def get_data(self):
        """Return 3 random dataset to plot."""
        def data():
        	
            """Return 7 randint between 0 and 100."""
            return [randint(0, 100) for x in range(7)]

        return [data() for x in range(3)]

products_chart_json = ProductChartJSONView.as_view()
products_chart_json2 = ProductChart2JSONView.as_view()