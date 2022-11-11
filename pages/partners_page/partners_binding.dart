import 'package:get/instance_manager.dart';
import 'package:listdo/src/pages/partners_page/partners_controller.dart';

class PartnersBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => PartnersController());
  }
}
