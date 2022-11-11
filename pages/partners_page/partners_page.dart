import 'package:flutter/material.dart';
import 'package:get/get_state_manager/get_state_manager.dart';
import 'package:listdo/src/pages/partners_page/partners_controller.dart';

class PartnersPage extends StatelessWidget {
  const PartnersPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: GetBuilder<PartnersController>(
        init: PartnersController(),
        builder: (partnersController) {
          return const Center(
            child: Text('Partners'),
          );
        },
      )),
    );
  }
}
