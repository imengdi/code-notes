#include <iostream>
#include <vector>

#include "json11.h"

using namespace json11;

class Point {
 public:
  Point () : x(10), y(10) {}
  Point (int x, int y) : x(x), y(y) {}
  Json to_json() const { return Json::array { x, y }; }

 private:
  int x;
  int y;
};

void json11_basic() {
  const std::string simple_test =
      R"({"k1":"hello-json", "k2":412, "k3":["a",123,true,false,null]})";

  std::string err;
  const auto json = Json::parse(simple_test, err);

  if (!err.empty())
    std::cout << err << std::endl;
  else
    std::cout << "no error" << std::endl;

  std::cout << "k1: " << json["k1"].string_value() << std::endl;
  std::cout << "k2: " << json["k2"].dump() << std::endl;
  std::cout << "k2: " << json["k2"].int_value() << std::endl;
  std::cout << "k3: " << json["k3"].dump() << std::endl;

  for (auto &k : json["k3"].array_items()) {
    std::cout << "    - " << k.dump() << std::endl;
  }
}

void json11_object() {
  Json my_json = Json::object {
    { "key1", "value1" },
    { "key2", false },
    { "key3", Json::array { 1, 2, 3 } },
  };
  std::string json_str = my_json.dump();
  std::cout << json_str << std::endl;

  Json json = Json::array { Json::object { { "k", "v" } }, my_json };

  std::string str1 = json[0]["k"].string_value();
  std::cout << str1 << std::endl;

  std::string str2 = json[1]["key1"].string_value();
  std::cout << str2 << std::endl;

  std::cout << json.dump() << std::endl;
}

void json11_advance() {
  Point dp;
  std::string points_json = Json(dp).dump();
  std::cout << points_json << std::endl;

  std::vector<Point> points = { { 1, 2 }, { 10, 20 }, { 100, 200 }, dp };
  points_json = Json(points).dump();
  std::cout << points_json << std::endl;
}

int main(int argc, char **argv) {
  json11_basic();
  json11_object();
  json11_advance();

  return 0;
}
