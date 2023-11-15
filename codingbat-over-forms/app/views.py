from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from .forms import FontTimesForm, NoTeenSumForm, XYZThereForm, CenteredAverageForm


# Create your views here.
def font_times_view(request: HttpRequest) -> HttpResponse:
    form = FontTimesForm()
    if request.GET:
        form = FontTimesForm(request.GET)
        if form.is_valid():
            phrase = form.cleaned_data["phrase"]
            copies = form.cleaned_data["copies"]

            if len(phrase) > 2:
                phrase = phrase[:3]

            phrase = phrase * copies

            return render(request, "result.html", context={"result": phrase})

    return render(request, "font_times.html", context={"form": form})


def no_teen_sum_view(request: HttpRequest) -> HttpResponse:
    form = NoTeenSumForm()
    if request.GET:
        form = NoTeenSumForm(request.GET)
        if form.is_valid():
            a = fix_teen(form.cleaned_data["a"])
            b = fix_teen(form.cleaned_data["b"])
            c = fix_teen(form.cleaned_data["c"])

            result = a + b + c

            return render(request, "result.html", context={"result": result})

    return render(request, "no_teen_sum.html", context={"form": form})


def fix_teen(n) -> int:
    if (n in range(13, 20)) and (n not in range(15, 17)):
        return 0
    else:
        return n


def xyz_there_view(request: HttpRequest) -> HttpResponse:
    form = XYZThereForm()
    if request.GET:
        form = XYZThereForm(request.GET)
        if form.is_valid():
            phrase = form.cleaned_data["phrase"]

            result = xyz_there(phrase)

            return render(request, "result.html", context={"result": result})

    return render(request, "xyz_there.html", context={"form": form})


def xyz_there(phrase: str) -> bool:
    if "xyz" not in phrase.lower():
        return False

    state = False

    for char in range(0, len(phrase)):
        if phrase[char] == "x":
            if phrase[char + 1] == "y":
                if phrase[char + 2] == "z":
                    if phrase != 0:
                        if phrase[char - 1] == ".":
                            state = False
                        else:
                            state = True
                    else:
                        state = True

    return state


def centered_average_view(request: HttpRequest) -> HttpResponse:
    form = CenteredAverageForm()
    if request.GET:
        form = CenteredAverageForm(request.GET)
        if form.is_valid():
            num_one = form.cleaned_data["num_one"]
            num_two = form.cleaned_data["num_two"]
            num_three = form.cleaned_data["num_three"]
            num_four = form.cleaned_data["num_four"]
            num_five = form.cleaned_data["num_five"]

            nums = [num_one, num_two, num_three, num_four, num_five]

            nums.remove(max(nums))
            nums.remove(min(nums))

            result = sum(nums) // len(nums)

            return render(request, "result.html", context={"result": result})

    return render(request, "centered_average.html", context={"form": form})
