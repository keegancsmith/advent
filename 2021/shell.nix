{ pkgs ? import <nixpkgs> { } }:
pkgs.mkShell { nativeBuildInputs = [ pkgs.nix pkgs.zls ]; }
