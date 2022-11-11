import 'package:get/instance_manager.dart';
import 'package:placeholders/src/placeholder_controller.dart';

class PlaceholderBinding extends Bindings {
  @override
  void dependencies() {
    Get.lazyPut(() => PlaceholderController());
  }
}
