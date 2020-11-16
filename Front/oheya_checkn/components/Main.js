import * as React from "react";
import { Header } from "react-native-elements";
import { SafeAreaProvider, SafeAreaView } from "react-native-safe-area-context";
import { Text, StatusBar, Button, StyleSheet } from "react-native";

export default () => {
    return (
        <SafeAreaView style={[{ backgroundColor: "#2089dc" }]}>
            <Header
                statusBarProps={{
                    barStyle: "light-content",
                    backgroundColor: "#2089dc"
                }}
                barStyle="light-content"
                placement="center"
                leftComponent={{ icon: "home", color: "#fff", hidden: false }}
                centerComponent={{
                    icon: "home",
                    text: "お部屋チェックン",
                    style: { color: "#fff", fontSize: 18, fontWeight: "900" }
                }}
            />
        </SafeAreaView>
    );
};
