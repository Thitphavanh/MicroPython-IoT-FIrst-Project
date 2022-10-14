import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'PHENOMENAL INC.'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int counter = 0;
  var message = 'ສະແດງຂໍ້ຄວາມ';
  TextEditingController textController = TextEditingController();

  void incrementCounter() {
    setState(() {
      counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        foregroundColor: Colors.redAccent,
        elevation: 0,
        title: Text(widget.title),
      ),
      body: SingleChildScrollView(
        child: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Image.asset(
                  'assets/images/image.jpg',
                  // 'https://cdn.dribbble.com/users/1622791/screenshots/11174104/flutter_intro.png',
                  height: 300.0,
                  width: Size.infinite.width,
                  fit: BoxFit.cover,
                ),
              ),
              const SizedBox(height: 8.0),
              const Text(
                'IoT Projects',
                style:  TextStyle(
                  color: Colors.redAccent,
                  fontSize: 18.0,
                ),
              ),
              Text(
                '$counter',
                style: Theme.of(context).textTheme.headline4,
              ),
              const SizedBox(height: 16.0),
              TextField(
                controller: textController,
                decoration: const InputDecoration(
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16.0),
              ElevatedButton.icon(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.redAccent,
                ),
                onPressed: () {
                  setState(() {
                    message = textController.text;
                  });
                },
                label: const Text('Enter'),
                icon: const Icon(Icons.flutter_dash),
              ),
              const SizedBox(height: 16.0),
              Text(
                message,
                style: const TextStyle(
                  color: Colors.black,
                  fontSize: 18.0,
                ),
              ),
            ],
          ),
        ),
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: incrementCounter,
        tooltip: 'Increment',
        child: const Icon(Icons.add),
      ),
    );
  }
}
