Name:		python-transformers
Version:	5.15.0
Release:	2
Summary:	State-of-the-art Machine Learning for PyTorch
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/huggingface/transformers
Source0:	https://files.pythonhosted.org/packages/source/t/transformers/transformers-%{version}.tar.gz
# 5.15.0 pins tokenizers<=0.23.0; 0.23.0 was never released on PyPI
Patch0:		transformers-5.15.0-tokenizers-0.23.1.patch
# Apertus 1.5 (apertus1p5) is not in a released Transformers yet.
# Backport of swiss-ai/transformers@3797303 (the pin on the model card),
# including WavTokenizer which the 1.5 audio tower requires.
Patch1:		transformers-5.15.0-apertus1p5.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)

%description
Transformers provides APIs and tools to easily download and train
state-of-the-art pretrained models for text, vision, audio and
multimodal tasks.

%files
%doc README.md
%license LICENSE
%{_bindir}/transformers
%{py_sitedir}/transformers
%{py_sitedir}/transformers-*.*-info
