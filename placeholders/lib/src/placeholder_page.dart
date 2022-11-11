import 'package:flutter/material.dart';
import 'package:get/get_state_manager/get_state_manager.dart';
import 'package:placeholders/src/placeholder_controller.dart';

class PlaceholderPage extends StatelessWidget {
  const PlaceholderPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: GetBuilder<PlaceholderController>(
        init: PlaceholderController(),
        builder: (PlaceholderController) {
          return const Center(
            child: Text('Placeholder'),
          );
        },
      )),
    );
  }
}
