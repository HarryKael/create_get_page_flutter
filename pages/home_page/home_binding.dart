import 'package:get/instance_manager.dart';
import 'package:listdo/src/pages/home_page/home_controller.dart';

class HomeBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => HomeController());
  }
}
