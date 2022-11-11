import 'package:flutter/material.dart';
import 'package:get/get_state_manager/get_state_manager.dart';
import 'package:listdo/src/pages/home_page/home_controller.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
          child: GetBuilder<HomeController>(
        init: HomeController(),
        builder: (homeController) {
          return const Center(
            child: Text('Home'),
          );
        },
      )),
    );
  }
}
