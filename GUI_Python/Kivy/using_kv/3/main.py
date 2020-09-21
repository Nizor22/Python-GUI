from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
	btn = ObjectProperty(None)

	def on_touch_down(self, touch):
		self.btn.opacity = .5
		print('Mouse Down', touch)

	def on_touch_move(self, touch):
		print('Mouse move', touch)

	def on_touch_up(self, touch):
		self.btn.opacity = 1
		print('Mouse up', touch)


class MyApp(App):
	def build(self):
		return Touch()


if __name__ == "__main__":
	MyApp().run()
