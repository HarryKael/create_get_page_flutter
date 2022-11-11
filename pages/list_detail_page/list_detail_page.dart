import 'package:flutter/material.dart';
import 'package:get/get_state_manager/get_state_manager.dart';
import 'package:listdo/src/pages/list_detail_page/list_detail_controller.dart';

class ListDetailPage extends StatelessWidget {
  const ListDetailPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: GetBuilder<ListDetailController>(
        init: ListDetailController(),
        builder: (listDetailController) {
          return const Center(
            child: Text('ListDetail'),
          );
        },
      )),
    );
  }
}
