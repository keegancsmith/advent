{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell { nativeBuildInputs = [ pkgs.zig pkgs.zls ]; }
