import 'package:get/instance_manager.dart';
import 'package:listdo/src/pages/list_detail_page/list_detail_controller.dart';

class ListDetailBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => ListDetailController());
  }
}
